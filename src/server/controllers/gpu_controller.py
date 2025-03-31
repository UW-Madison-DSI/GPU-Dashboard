################################################################################
#                                                                              #
#                              gpu_controller.py                               #
#                                                                              #
################################################################################
#                                                                              #
#        This controller is used to handle requests for gpu use info.          #
#                                                                              #
#        Author(s): Abe Megahed                                                #
#                                                                              #
################################################################################
#     Copyright (C) 2025, Data Science Institute, University of Wisconsin      #
################################################################################

import datetime
import flask
from flask import request
from controllers.controller import Controller
from models.gpu import Gpu

class GpuController(Controller):

	#
	# posting methods
	#

	@staticmethod
	def post_create(db):

		# parse parameters
		#
		host = request.form.get('host')
		gpu = request.form.get('gpu')
		pid = request.form.get('pid')
		user = request.form.get('user')
		gpu_memory = request.form.get('gpu_memory')
		percent_cpu = request.form.get('percent_cpu')
		percent_memory = request.form.get('percent_memory')
		time = request.form.get('time')
		command = request.form.get('command')

		# create gpu log object
		#
		gpu = Gpu({
			'host': host,
			'gpu': gpu,
			'pid': pid,
			'user': user,
			'gpu_memory': gpu_memory,
			'percent_cpu': percent_cpu,
			'percent_memory': percent_memory,
			'time': time,
			'command': command,
			'created_at': datetime.datetime.now()
		})

		# store data
		#
		connection = Controller.connect(db)
		gpu.save(connection)
		connection.close()

		# return response
		#
		return 'OK', 200

	#
	# getting methods
	#

	@staticmethod
	def get_hosts(db):

		# fetch data from database
		#
		connection = GpuController.connect(db)
		cursor = connection.cursor()
		query = 'SELECT DISTINCT host FROM gpus';
		cursor.execute(query)
		data = cursor.fetchall()
		cursor.close()
		connection.close()

		# format data
		#
		hosts = []
		for item in data:
			hosts.append(item[0])
		return hosts

	@staticmethod
	def get_latest_time(db, host):
		gpu = Gpu()

		# fetch time from database
		#
		connection = Controller.connect(db)
		cursor = connection.cursor()
		query = 'SELECT MAX(created_at) FROM ' + gpu.table + ' WHERE host="' + host + '" LIMIT 1'
		cursor.execute(query)
		latest_time = cursor.fetchone()
		cursor.close() 
		connection.close()

		# format time
		#
		time_str = latest_time[0].strftime('%Y-%m-%d %H:%M') if (latest_time[0]) else None
		return time_str

	@staticmethod
	def get_latest_gpus_by_host(db, host):
		gpu = Gpu()

		# get most recent time logged for this host
		#
		time_str = GpuController.get_latest_time(db, host)

		# get rows at most recent time
		#
		if (time_str):

			# fetch data from database
			#
			connection = Controller.connect(db)
			cursor = connection.cursor()
			query = 'SELECT id, host, gpu, pid, user, gpu_memory, percent_cpu, percent_memory, time, command, created_at FROM ' + gpu.table + ' WHERE created_at >="' + time_str + '" AND host="' + host + '"'
			cursor.execute(query)
			data = cursor.fetchall()
			cursor.close()
			connection.close()
		else:
			data = None

		# format data
		#
		array = []
		if (data):
			for item in data:
				array.append({
					'id': item[0],
					'host': item[1],
					'gpu': item[2],
					'pid': item[3],
					'user': item[4],
					'gpu_memory': item[5],
					'percent_cpu': item[6],
					'percent_memory': item[7],
					'time': str(item[8]) if (item[8]) else None,
					'command': item[9],
					'created_at': str(item[10])
				})

		return array

	@staticmethod
	def get_latest_gpus(db):

		# parse parameters
		#
		host = request.args.get('host')

		if (host):
			return GpuController.get_latest_gpus_by_host(db, host)
		else:
			array = []
			hosts = GpuController.get_hosts(db)
			for host in hosts:
				gpus = GpuController.get_latest_gpus_by_host(db, host)
				array += gpus
			return array


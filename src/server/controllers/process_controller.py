################################################################################
#                                                                              #
#                            process_controller.py                             #
#                                                                              #
################################################################################
#                                                                              #
#        This controller is used to handle requests for process info.          #
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
from models.process import Process

class ProcessController(Controller):

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

		# create process object
		#
		process = Process({
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
		process.save(connection)
		connection.close()

		# return response
		#
		return 'OK', 200

	#
	# getting methods
	#

	@staticmethod
	def get_hosts(db):
		process = Process()

		# fetch data from database
		#
		connection = Controller.connect(db)
		cursor = connection.cursor()
		query = 'SELECT DISTINCT host FROM ' + process.table;
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
		process = Process()

		# fetch time from database
		#
		connection = Controller.connect(db)
		cursor = connection.cursor()
		query = 'SELECT MAX(created_at) FROM ' + process.table + ' WHERE host="' + host + '" LIMIT 1'
		cursor.execute(query)
		latest_time = cursor.fetchone()
		cursor.close() 
		connection.close()

		# format time
		#
		time_str = latest_time[0].strftime('%Y-%m-%d %H:%M') if (latest_time[0]) else None
		return time_str

	@staticmethod
	def get_latest_by_host(db, host):
		process = Process()

		# get most recent time logged for this host
		#
		time_str = ProcessController.get_latest_time(db, host)

		# get rows at most recent time
		#
		if (time_str):

			# fetch data from database
			#
			connection = Controller.connect(db)
			cursor = connection.cursor()
			query = 'SELECT id, host, gpu, pid, user, gpu_memory, percent_cpu, percent_memory, time, command, created_at FROM ' + process.table + ' WHERE created_at >="' + time_str + '" AND host="' + host + '"'
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
	def get_latest(db):

		# parse parameters
		#
		host = request.args.get('host')

		if (host):
			return ProcessController.get_latest_by_host(db, host)
		else:
			array = []
			hosts = ProcessController.get_hosts(db)
			for host in hosts:
				array += ProcessController.get_latest_by_host(db, host)
			return array


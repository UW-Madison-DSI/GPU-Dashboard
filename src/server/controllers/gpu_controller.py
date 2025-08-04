################################################################################
#                                                                              #
#                              gpu_controller.py                               #
#                                                                              #
################################################################################
#                                                                              #
#        This controller is used to handle requests for gpu info.              #
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
	# getting methods
	#

	@staticmethod
	def get_hosts(connection):
	
		# check params
		#
		if connection is None:
			return []

		# create query
		#
		gpu = Gpu()
		query = 'SELECT DISTINCT host FROM ' + gpu.table;

		# execute query
		#
		cursor = connection.cursor()
		cursor.execute(query)
		data = cursor.fetchall()
		cursor.close()

		# format data
		#
		hosts = []
		for item in data:
			hosts.append(item[0])
		return hosts

	@staticmethod
	def get_latest_time(connection, host):

		# check params
		#
		if connection is None or host is None:
			return []

		# create query 
		#
		gpu = Gpu()
		query = 'SELECT MAX(created_at) FROM ' + gpu.table + ' WHERE host="' + host + '" LIMIT 1'

		# execute query
		#
		cursor = connection.cursor()
		cursor.execute(query)
		latest_time = cursor.fetchone()
		cursor.close() 

		# format time
		#
		time_str = latest_time[0].strftime('%Y-%m-%d %H:%M') if (latest_time[0]) else None
		return time_str

	@staticmethod
	def get_latest_by_host(connection, host):

		# check params
		#
		if connection is None or host is None:
			return []

		# get most recent time logged for this host
		#
		time_str = GpuController.get_latest_time(connection, host)

		# get rows at most recent time
		#
		if (time_str):

			# create query
			#
			gpu = Gpu()
			query = 'SELECT id, host, gpu, temp, power, memory, gpu_util, created_at FROM ' + gpu.table + ' WHERE created_at >="' + time_str + '" AND host="' + host + '"'

			# execute query
			#
			cursor = connection.cursor()
			cursor.execute(query)
			data = cursor.fetchall()
			cursor.close()
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
					'temp': item[3],
					'power': item[4],
					'memory': item[5],
					'gpu_util': item[6],
					'created_at': str(item[7])
				})

		return array

	#
	# route handling methods
	#

	@staticmethod
	def post_create(db):

		# connect to database
		#
		connection = Controller.connect(db)
		if connection is None:
			return 'Could not connect to database', 500

		# parse parameters
		#
		host = request.form.get('host')
		gpu = request.form.get('gpu')
		temp = request.form.get('temp')
		power = request.form.get('power')
		memory = request.form.get('memory')
		gpu_util = request.form.get('gpu_util')

		# create process object
		#
		gpu = Gpu({
			'host': host,
			'gpu': gpu,
			'temp': temp,
			'power': power,
			'memory': memory,
			'gpu_util': gpu_util,
			'created_at': datetime.datetime.now()
		})

		# store data
		#
		gpu.save(connection)
		connection.close()

		# return response
		#
		return 'OK', 200

	@staticmethod
	def get_latest(db):
		results = []

		# connect to database
		#
		connection = Controller.connect(db)
		if connection is None:
			return 'Could not connect to database', 500

		# parse parameters
		#
		host = request.args.get('host')

		if (host):
			results = GpuController.get_latest_by_host(connection, host)
		else:
			hosts = GpuController.get_hosts(connection)
			for host in hosts:
				results += GpuController.get_latest_by_host(connection, host)

		connection.close()
		return results

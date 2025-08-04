################################################################################
#                                                                              #
#                            storage_controller.py                             #
#                                                                              #
################################################################################
#                                                                              #
#        This controller is used to handle requests for storage info.          #
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
from models.storage import Storage

class StorageController(Controller):

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
		storage = Storage()
		query = 'SELECT DISTINCT host FROM ' + storage.table;

		# execute query
		#
		cursor = connection.cursor()
		cursor.execute(query)
		data = cursor.fetchall()

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
			return

		# create query
		#
		storage = Storage()
		query = 'SELECT MAX(created_at) FROM ' + storage.table + ' WHERE min_age IS NULL AND max_age IS NULL AND host="' + host + '" LIMIT 1'

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
	def get_younger_time(connection, host, max_age):

		# check params
		#
		if connection is None or host is None:
			return

		# crete query
		#
		storage = Storage()
		query = 'SELECT MAX(created_at) FROM ' + storage.table + ' WHERE host="' + host + '" AND max_age = ' + max_age + ' LIMIT 1'

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
	def get_older_time(connection, host, min_age):

		# check params
		#
		if connection is None or host is None:
			return

		# create query
		#
		storage = Storage()
		query = 'SELECT MAX(created_at) FROM ' + storage.table + ' WHERE host="' + host + '" AND min_age = ' + min_age + ' LIMIT 1'

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
		time_str = StorageController.get_latest_time(connection, host)

		# get rows at most recent time
		#
		if (time_str):

			# create query
			#
			storage = Storage()
			query = 'SELECT id, host, directory, size, created_at FROM ' + storage.table + ' WHERE min_age IS NULL AND max_age IS NULL AND created_at >="' + time_str + '" AND host="' + host + '"'

			# execute query
			#
			cursor = connection.cursor()
			cursor.execute(query)
			data = cursor.fetchall()
			cursor.close()
		else:
			data = None

		# format database fields
		#
		array = []
		if (data):
			for item in data:
				array.append({
					'id': item[0],
					'host': item[1],
					'directory': item[2],
					'size': item[3],
					'created_at': str(item[4])
				})

		return array

	@staticmethod
	def get_younger_by_host(connection, host, max_age):

		# check params
		#
		if connection is None or host is None:
			return []

		# get most recent time logged for this host
		#
		time_str = StorageController.get_younger_time(connection, host, max_age)

		# get rows at most recent time
		#
		if (time_str):

			# create query
			#
			storage = Storage()
			query = 'SELECT id, host, directory, size, created_at FROM ' + storage.table + ' WHERE max_age = ' + str(max_age) + ' AND created_at >="' + time_str + '" AND host="' + host + '"'

			# execute query
			#
			cursor = connection.cursor()
			cursor.execute(query)
			data = cursor.fetchall()
			cursor.close()
		else:
			data = None

		# format database fields
		#
		array = []
		if (data):
			for item in data:
				array.append({
					'id': item[0],
					'host': item[1],
					'directory': item[2],
					'size': item[3],
					'created_at': str(item[4])
				})

		return array

	@staticmethod
	def get_older_by_host(connection, host, min_age):
		
		# check params
		#
		if connection is None or host is None:
			return []

		# get most recent time logged for this host
		#
		time_str = StorageController.get_older_time(connection, host, min_age)

		# get rows at most recent time
		#
		if (time_str):

			# create query
			#
			storage = Storage()
			query = 'SELECT id, host, directory, size, created_at FROM ' + storage.table + ' WHERE min_age = ' + str(min_age) + ' AND created_at >="' + time_str + '" AND host="' + host + '"'

			# execute query
			#
			cursor = connection.cursor()
			cursor.execute(query)
			data = cursor.fetchall()
			cursor.close()
		else:
			data = None

		# format database fields
		#
		array = []
		if (data):
			for item in data:
				array.append({
					'id': item[0],
					'host': item[1],
					'directory': item[2],
					'size': item[3],
					'created_at': str(item[4])
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
		if not connection:
			return "Could not connect to database.", 500

		# parse parameters
		#
		host = request.form.get('host')
		directory = request.form.get('directory')
		size = request.form.get('size')
		min_age = request.form.get('min_age')
		max_age = request.form.get('max_age')

		# create gpu log object
		#
		storage = Storage({
			'host': host,
			'directory': directory,
			'size': size,
			'min_age': min_age,
			'max_age': max_age,
			'created_at': datetime.datetime.now()
		})

		# store data
		#
		storage.save(connection)
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
			results = StorageController.get_latest_by_host(connection, host)
		else:
			hosts = StorageController.get_hosts(connection)
			for host in hosts:
				results += StorageController.get_latest_by_host(connection, host)

		connection.close()
		return results

	@staticmethod
	def get_younger(db, max_age):
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
			results = StorageController.get_younger_by_host(connection, host, max_age)
		else:
			hosts = StorageController.get_hosts(connection)
			for host in hosts:
				results += StorageController.get_younger_by_host(connection, host, max_age)

		connection.close()
		return results

	@staticmethod
	def get_older(db, min_age):
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
			results = StorageController.get_older_by_host(connection, host, min_age)
		else:
			hosts = StorageController.get_hosts(connection)
			for host in hosts:
				storage = StorageController.get_older_by_host(connection, host, min_age)
				results += storage

		connection.close()
		return results

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
from models.storage import Storage

class StorageController:

	#
	# posting methods
	#

	@staticmethod
	def post_create(db):

		# parse parameters
		#
		host = request.form.get('host')
		amount = request.form.get('amount')
		directory = request.form.get('directory')

		# create gpu log object
		#
		storage = Storage({
			'host': host,
			'amount': amount,
			'directory': directory,
			'created_at': datetime.datetime.now()
		})

		# store data
		#
		storage.save(db)

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
		cursor = db.cursor()
		query = 'SELECT DISTINCT host FROM gpus';
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
	def get_latest_time(db, host):
		storage = Storage()

		# fetch time from database
		#
		cursor = db.cursor()
		query = 'SELECT MAX(created_at) FROM ' + storage.table + ' WHERE host="' + host + '" LIMIT 1'
		cursor.execute(query)
		latest_time = cursor.fetchone()
		cursor.close() 

		# format time
		#
		time_str = latest_time[0].strftime('%Y-%m-%d %H:%M:%S') if (latest_time[0]) else None
		return time_str

	@staticmethod
	def get_latest_storage_by_host(db, host):
		storage = Storage()

		# get most recent time logged for this host
		#
		time_str = StorageController.get_latest_time(db, host)

		# get rows at most recent time
		#
		if (time_str):

			# fetch data from database
			#
			cursor = db.cursor()
			query = 'SELECT id, host, amount, directory FROM ' + storage.table + ' WHERE created_at="' + time_str + '" AND host="' + host + '"'
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
					'amount': item[2],
					'directory': item[3]
				})

		return array

	@staticmethod
	def get_latest_storage(db):

		# parse parameters
		#
		host = request.args.get('host')

		if (host):
			return StorageController.get_latest_storage_by_host(db, host)
		else:
			array = []
			hosts = StorageController.get_hosts(db)
			for host in hosts:
				storage = StorageController.get_latest_storage_by_host(db, host)
				array += storage
			return array


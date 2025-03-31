################################################################################
#                                                                              #
#                                controller.py                                 #
#                                                                              #
################################################################################
#                                                                              #
#        This is a base class which is used to handle requests for info.       #
#                                                                              #
#        Author(s): Abe Megahed                                                #
#                                                                              #
################################################################################
#     Copyright (C) 2025, Data Science Institute, University of Wisconsin      #
################################################################################

import mysql.connector

class Controller:

	def connect(db):

		# connect to database
		#
		try:
			connection = mysql.connector.connect(
				host = db['host'],
				port = db['port'],
				username = db['username'],
				password = db['password'],
				database = db['database']
			)
		except Exception as e:
			print("Could not connect to database.")
			print(str(e))
			exit()

		return connection


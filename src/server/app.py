################################################################################
#                                                                              #
#                                    app.py                                    #
#                                                                              #
################################################################################
#                                                                              #
#        This is a web server for managing GPU resource information.           #
#                                                                              #
#        Author(s): Abe Megahed                                                #
#                                                                              #
################################################################################
#     Copyright (C) 2025, Data Science Institute, University of Wisconsin      #
################################################################################

import config
import mysql.connector
from flask import Flask
from controllers.gpu_controller import GpuController
from controllers.process_controller import ProcessController
from controllers.storage_controller import StorageController
from flask_cors import CORS

################################################################################
#                                   globals                                    #
################################################################################
local = False

if (local):
	db = {
		'host': 'localhost',
		'port': 3306,
		'username': 'root',
		'password': 'root',
		'database': 'dashboard'
	}
else:
	db = {
		'host': 'db',
		'port': 3306,
		'username': 'webuser',
		'password': 'password',
		'database': 'dashboard'	
	}

################################################################################
#                                initialization                                #
################################################################################

app = Flask(__name__)
CORS(app)

# configure app fron config.py
app.config.from_object(config)

################################################################################
#                                    routes                                    #
################################################################################

#
# post routes
#

@app.post('/gpus')
def post_gpu():

	"""
	Post gpu information.

	Return
		object: The parsed gpu parameters.
	"""

	return GpuController.post_create(db)

@app.post('/processes')
def post_process():

	"""
	Post gpu information.

	Return
		object: The parsed gpu parameters.
	"""

	return ProcessController.post_create(db)

@app.post('/storage')
def post_storage():

	"""
	Post storage information.

	Return
		object: The parsed storage parameters.
	"""

	return StorageController.post_create(db)

#
# get routes
#

@app.get('/')
def get_test():

	"""
	Get test information.

	Return
		string.
	"""

	return "<h1>Welcome to the GPU Dashboard Server!</h1>"

@app.get('/hosts')
def get_hosts():

	"""
	Get host information.

	Return
		list of host names.
	"""

	return ProcessController.get_hosts(db)

@app.get('/gpus/latest')
def get_latest_gpus():

	"""
	Post most recent GPU information.

	Return
		list of gpu info.
	"""

	return GpuController.get_latest(db)

@app.get('/processes/latest')
def get_latest_processes():

	"""
	Post most recent GPU process information.

	Return
		list of process info.
	"""

	return ProcessController.get_latest(db)

@app.get('/storage/latest')
def get_latest_storage():

	"""
	Get most recent storage information.

	Return
		list of storage info.
	"""

	return StorageController.get_latest(db)

################################################################################
#                                     main                                     #
################################################################################

if __name__ == '__main__':
	app.debug = True

	if (app.config['PORT'] == 443):
		app.run(host=app.config['HOST'], port=443, ssl_context=(app.config['SSL_CERT'], app.config['SSL_KEY']))
	else:
		app.run(host=app.config['HOST'], port=app.config['PORT'])
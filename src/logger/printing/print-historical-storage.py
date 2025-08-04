################################################################################
#                                                                              #
#                              report-storage.py                               #
#                                                                              #
################################################################################
#                                                                              #
#        This is a utility for reporting storage usage statistics.             #
#                                                                              #
#        Author(s): Abe Megahed                                                #
#                                                                              #
#        This file is subject to the terms and conditions defined in           #
#        'LICENSE.txt', which is part of this source code distribution.        #
#                                                                              #
################################################################################
#     Copyright (C) 2025, Data Science Institute, University of Wisconsin      #
################################################################################

import sys
import requests
from report_storage import run_command
from report_storage import get_largest_directories
from report_storage import get_free_space

#
# variables
#

# url = 'https://olvi-dashboard-api.services.dsi.wisc.edu'
url = 'http://localhost:5000'

#
# directory size getting functions
#

def get_directory_size_younger_than(directory, max_days_old):
	command = 'find ' + directory + ' -type f -mtime -' + str(max_days_old) + ' -print0 | du -hc --files0-from - | tail -n 1'
	output = run_command(command)
	terms = output[0].split()
	return terms[0]

def get_directory_size_older_than(directory, min_days_old):
	command = 'find ' + directory + ' -type f -mtime +' + str(min_days_old) + ' -print0 | du -hc --files0-from - | tail -n 1'
	output = run_command(command)
	terms = output[0].split()
	return terms[0]

#
# directory getting functions
#

def get_largest_directories_younger_than(max_number, max_days_old):
	data = []
	directories = get_largest_directories(max_number)
	for directory in directories:
		dirname = directory['directory']

		# add directory size by age
		#
		data.append({
			'host': platform.node(),
			'directory': dirname,
			'size': get_directory_size_younger_than(dirname, max_days_old),
			'max_age': max_days_old
		})

	return data

def get_largest_directories_older_than(max_number, min_days_old):
	data = []
	directories = get_largest_directories(max_number)
	for directory in directories:
		dirname = directory['directory']

		# add directory size by age
		#
		data.append({
			'host': platform.node(),
			'directory': dirname,
			'size': get_directory_size_older_than(dirname, min_days_old),
			'min_age': min_days_old
		})

	return data

#
# main
#

if __name__ == '__main__':

	min_days_old = 30
	print("finding largest directories more than ", min_days_old, " days old.", sep='')
	data = get_largest_directories_older_than(10, min_days_old)
	for item in data:
		print(item)

	min_days_old = 90
	print("finding largest directories more than ", min_days_old, " days old.", sep='')
	data = get_largest_directories_older_than(10, min_days_old)
	for item in data:
		print(item)

	min_days_old = 180
	print("finding largest directories more than ", min_days_old, " days old.", sep='')
	data = get_largest_directories_older_than(10, min_days_old)
	for item in data:
		print(item)

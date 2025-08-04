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
import platform
import subprocess

#
# variables
#

# url = 'https://olvi-dashboard-api.services.dsi.wisc.edu'
url = 'http://localhost:5000'

#
# functions
#

def run_command(command):

	"""
	Runs a shell command and returns its output lines as a list.

	Args:
		command: The shell command to run (string).

	Returns:
		A list of strings, where each string is a line of the command's output.
		Returns None if the command fails.
	"""

	try:
		process = subprocess.run(command, shell=True, capture_output=True, text=True)
		output_lines = process.stdout.splitlines()
		return output_lines
	except subprocess.CalledProcessError as e:
		print(f"Command failed with error: {e}")
		print(f"Stderr: {e.stderr}")
		return None

#
# directory getting functions
#

def get_largest_directories(max_number):

	"""
	Parse stats from lines of text.

	Args:
		command: The shell command to run (string).

	Returns:
		A list of strings, where each string is a line of the command's output.
		Returns None if the command fails.
	"""

	command = 'du -hs /data/* | sort -rh | head -' + str(max_number)
	lines = run_command(command)
	data = []
	count = 0
	for line in lines:
		count += 1

		# break line by whitespace
		#
		items = line.split()

		# parse individual fields
		#
		data.append({
			'host': platform.node(),
			'size': items[0],
			'directory': items[1]
		})

	return data

def get_free_space():

	"""
	Parse stats from lines of text.

	Args:
		command: The shell command to run (string).

	Returns:
		A list of strings, where each string is a line of the command's output.
		Returns None if the command fails.
	"""

	lines = run_command('df -h /data')
	items = lines[1].split()

	# parse individual fields
	#
	return {
		'host': platform.node(),
		'directory': 'free',
		'size': items[3]
	}

#
# main
#

if __name__ == '__main__':

	print("finding largest directories...")
	data = get_largest_directories(10)
	data.append(get_free_space())

	# export data
	#
	for item in data:
		# print(item)
		response = requests.post(url + '/storage', data=item)
		print(response)

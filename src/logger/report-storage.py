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

import requests
import platform
import subprocess

#
# variables
#

url = 'https://olvi-dashboard-api.services.dsi.wisc.edu/storage'

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
# functions
#

def parse_stats(lines):

	"""
	Parse stats from lines of text.

	Args:
		command: The shell command to run (string).

	Returns:
		A list of strings, where each string is a line of the command's output.
		Returns None if the command fails.
	"""

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
			'amount': items[0],
			'directory': items[1]
		})

	return data

def parse_avail(line):

	"""
	Parse stats from lines of text.

	Args:
		command: The shell command to run (string).

	Returns:
		A list of strings, where each string is a line of the command's output.
		Returns None if the command fails.
	"""

	items = line.split()

	# parse individual fields
	#
	return {
		'host': platform.node(),
		'amount': items[3],
		'directory': 'free'
	}

#
# main
#

if __name__ == '__main__':
	lines = run_command('du -hs /data/* | sort -rh | head -10')
	data = parse_stats(lines)
	lines = run_command('df -h /data')
	data.append(parse_avail(lines[1]))

	for item in data:
		print(item)
		# response = requests.post(url, data=item)
		# print(response)

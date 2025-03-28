################################################################################
#                                                                              #
#                                report-gpus.py                                #
#                                                                              #
################################################################################
#                                                                              #
#        This is a utility for reporting gpu usage statistics.                 #
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

url = 'https://olvi-dashboard-api.services.dsi.wisc.edu/gpu'

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

def parse_file(filename):

	"""
	Parse lines of text from file.

	Args:
		filename: The file to parse.

	Returns:
		A list of strings.
	"""

	lines = []
	with open(filename, "r") as file:
		count = 0
		for line in file:
			lines.append(line)
	return lines

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

		# parse each line
		#
		if (count > 43 and not line.startswith('+')):
			line = line[2:-2]

			# break line by whitespace
			#
			items = line.split()

			# parse individual fields
			#
			data.append({
				'host': platform.node(),
				'gpu': int(items[0]),
				'pid': int(items[1]),
				'user': items[2],
				'gpu_memory': int(items[3].replace('MiB', '')),
				'percent_cpu': items[4],
				'percent_memory': items[5],
				'time': items[6],
				'command': ' '.join(items[7:])
			})

	return data

#
# main
#

if __name__ == '__main__':
	lines = run_command('nvidia-htop.py -l')
	data = parse_stats(lines)

	for item in data:
		# print(item)
		response = requests.post(url, data=item)
		print(response)
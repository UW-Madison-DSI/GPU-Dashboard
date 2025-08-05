################################################################################
#                                                                              #
#                                report-gpus.py                                #
#                                                                              #
################################################################################
#                                                                              #
#        This is a utility for reporting gpu statistics.                       #
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
from config import url

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

def parse_gpus(lines):

	"""
	Parse gpu stats from lines of text.

	Args:
		lines: The text lines to parse.

	Returns:
		An array of objects.
	"""

	gpus = []
	count = 0
	line_number = 9
	for gpu in range(0,8):
		line = lines[line_number]

		# strip start / end delimiters
		#
		line = line[2:-2]
		if (not line):
			continue

		# break line by whitespace
		#
		items = line.split()
		# print("ITEMS: ")
		# print(items)

		# parse individual fields
		#
		gpus.append({
			# 'host': 'olvi-2',
			'host': platform.node(),
			'gpu': gpu,
			'temp': int(items[1].replace('C', '')),
			'power': int(items[3].replace('W', '')),
			'memory': int(items[7].replace('MiB', '')),
			'gpu_util': int(items[11].replace('%', '')),
		})

		line_number += 4

	return gpus

#
# main
#

if __name__ == '__main__':
	# lines = parse_file('test/olvi1-output.txt')
	lines = run_command('/afs/cs.wisc.edu/u/a/m/amegahed/.local/bin/nvidia-htop.py -l')
	gpus = parse_gpus(lines)

	print();

	print("GPUs:")
	for gpu in gpus:
		# print("GPU:")
		# print(gpu)
		response = requests.post(url + '/gpus', data=gpu)
		print(response)
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

#
# variables
#

url = 'http://localhost:5000/gpu'

#
# functions
#

def parse_stats(filename):
	data = []
	with open(filename, "r") as file:
		count = 0
		for line in file:
			count += 1

			# parse each line
			#
			if (count > 2 and not line.startswith('+')):
				line = line[2:-2]

				# break line by whitespace
				#
				items = line.split()

				# parse individual fields
				#
				data.append({
					'host': platform.node(),
					'host': 'olvi-2',
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
	data = parse_stats('olvi2-gpu-usage.txt')

	for item in data:
		print(item)
		response = requests.post(url, data=item)
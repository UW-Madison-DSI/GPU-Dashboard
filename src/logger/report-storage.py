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

#
# variables
#

url = 'http://localhost:5000/storage'

#
# functions
#

def parse_stats(filename):
	data = []
	with open(filename, "r") as file:
		count = 0
		for line in file:

			# break line by whitespace
			#
			items = line.split()

			# parse individual fields
			#
			data.append({
				# 'host': platform.node(),
				'host': 'olvi-2',
				'amount': items[0],
				'directory': items[1]
			})

		return data

#
# main
#

if __name__ == '__main__':
	data = parse_stats('olvi2-storage.txt')

	for item in data:
		print(item)
		response = requests.post(url, data=item)

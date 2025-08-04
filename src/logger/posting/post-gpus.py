################################################################################
#                                                                              #
#                                 post-gpus.py                                 #
#                                                                              #
################################################################################
#                                                                              #
#        This is a utility for posting gpu statistics.                         #
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
from config import url

#
# functions
#

def post_gpus(gpus):
	for gpu in gpus:
		response = requests.post(url + '/gpus', data=gpu)
		print(response)

#
# main
#

if __name__ == '__main__':

	post_gpus([
		{'host': 'olvi-1', 'gpu': 0, 'temp': 27, 'power': 42, 'memory': 4, 'gpu_util': 0},
		{'host': 'olvi-1', 'gpu': 1, 'temp': 26, 'power': 41, 'memory': 4, 'gpu_util': 0},
		{'host': 'olvi-1', 'gpu': 2, 'temp': 27, 'power': 45, 'memory': 4, 'gpu_util': 0},
		{'host': 'olvi-1', 'gpu': 3, 'temp': 26, 'power': 44, 'memory': 1593, 'gpu_util': 0},
		{'host': 'olvi-1', 'gpu': 4, 'temp': 49, 'power': 220, 'memory': 31843, 'gpu_util': 99},
		{'host': 'olvi-1', 'gpu': 5, 'temp': 49, 'power': 179, 'memory': 31853, 'gpu_util': 98},
		{'host': 'olvi-1', 'gpu': 6, 'temp': 51, 'power': 205, 'memory': 31837, 'gpu_util': 100},
		{'host': 'olvi-1', 'gpu': 7, 'temp': 40, 'power': 194, 'memory': 15919, 'gpu_util': 58}
	])

	post_gpus([
		{'host': 'olvi-2', 'gpu': 0, 'temp': 27, 'power': 42, 'memory': 4, 'gpu_util': 0},
		{'host': 'olvi-2', 'gpu': 1, 'temp': 26, 'power': 41, 'memory': 4, 'gpu_util': 0},
		{'host': 'olvi-2', 'gpu': 2, 'temp': 27, 'power': 45, 'memory': 4, 'gpu_util': 0},
		{'host': 'olvi-2', 'gpu': 3, 'temp': 26, 'power': 44, 'memory': 1593, 'gpu_util': 0},
		{'host': 'olvi-2', 'gpu': 4, 'temp': 49, 'power': 220, 'memory': 31843, 'gpu_util': 99},
		{'host': 'olvi-2', 'gpu': 5, 'temp': 49, 'power': 179, 'memory': 31853, 'gpu_util': 98},
		{'host': 'olvi-2', 'gpu': 6, 'temp': 51, 'power': 205, 'memory': 31837, 'gpu_util': 100},
		{'host': 'olvi-2', 'gpu': 7, 'temp': 40, 'power': 194, 'memory': 15919, 'gpu_util': 58}
	])

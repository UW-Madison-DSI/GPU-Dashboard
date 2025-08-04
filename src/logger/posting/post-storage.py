################################################################################
#                                                                              #
#                               post-storage.py                                #
#                                                                              #
################################################################################
#                                                                              #
#        This is a utility for posting storage statistics.                     #
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

def post_data(data):
	for item in data:
		response = requests.post(url + '/storage', data=item)
		print(response)

#
# main
#

if __name__ == '__main__':

	post_data([
		{'host': 'olvi-1', 'size': '1.7T', 'directory': '/data/milawang'},
		{'host': 'olvi-1', 'size': '987G', 'directory': '/data/yzeng58'},
		{'host': 'olvi-1', 'size': '624G', 'directory': '/data/changho'},
		{'host': 'olvi-1', 'size': '548G', 'directory': '/data/rouhiainen'},
		{'host': 'olvi-1', 'size': '529G', 'directory': '/data/s_setup'},
		{'host': 'olvi-1', 'size': '502G', 'directory': '/data/yguo'},
		{'host': 'olvi-1', 'size': '492G', 'directory': '/data/linbo'},
		{'host': 'olvi-1', 'size': '462G', 'directory': '/data/sungjuncho'},
		{'host': 'olvi-1', 'size': '387G', 'directory': '/data/jifan'},
		{'host': 'olvi-1', 'size': '375G', 'directory': '/data/zhiqi'},
		{'host': 'olvi-1', 'directory': 'free', 'size': '17G'}
	])
	post_data([
		{'host': 'olvi-2', 'size': '1.7T', 'directory': '/data/milawang'},
		{'host': 'olvi-2', 'size': '987G', 'directory': '/data/yzeng58'},
		{'host': 'olvi-2', 'size': '624G', 'directory': '/data/changho'},
		{'host': 'olvi-2', 'size': '548G', 'directory': '/data/rouhiainen'},
		{'host': 'olvi-2', 'size': '529G', 'directory': '/data/s_setup'},
		{'host': 'olvi-2', 'size': '502G', 'directory': '/data/yguo'},
		{'host': 'olvi-2', 'size': '492G', 'directory': '/data/linbo'},
		{'host': 'olvi-2', 'size': '462G', 'directory': '/data/sungjuncho'},
		{'host': 'olvi-2', 'size': '387G', 'directory': '/data/jifan'},
		{'host': 'olvi-2', 'size': '375G', 'directory': '/data/zhiqi'},
		{'host': 'olvi-2', 'directory': 'free', 'size': '17G'}
	])
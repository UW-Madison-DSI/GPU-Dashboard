################################################################################
#                                                                              #
#                          post-historical-storage.py                          #
#                                                                              #
################################################################################
#                                                                              #
#        This is a utility for posting historical storage statistics.          #
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
		{'host': 'olvi-1', 'directory': '/data/milawang', 'size': '1.7T', 'min_age': 30},
		{'host': 'olvi-1', 'directory': '/data/yzeng58', 'size': '986G', 'min_age': 30},
		{'host': 'olvi-1', 'directory': '/data/changho', 'size': '623G', 'min_age': 30},
		{'host': 'olvi-1', 'directory': '/data/rouhiainen', 'size': '547G', 'min_age': 30},
		{'host': 'olvi-1', 'directory': '/data/s_setup', 'size': '529G', 'min_age': 30},
		{'host': 'olvi-1', 'directory': '/data/yguo', 'size': '502G', 'min_age': 30},
		{'host': 'olvi-1', 'directory': '/data/linbo', 'size': '492G', 'min_age': 30},
		{'host': 'olvi-1', 'directory': '/data/sungjuncho', 'size': '411G', 'min_age': 30},
		{'host': 'olvi-1', 'directory': '/data/jifan', 'size': '357G', 'min_age': 30},
		{'host': 'olvi-1', 'directory': '/data/zhiqi', 'size': '375G', 'min_age': 30}
	])

	post_data([
		{'host': 'olvi-1', 'directory': '/data/milawang', 'size': '1.6T', 'min_age': 90},
		{'host': 'olvi-1', 'directory': '/data/yzeng58', 'size': '958G', 'min_age': 90},
		{'host': 'olvi-1', 'directory': '/data/changho', 'size': '219G', 'min_age': 90},
		{'host': 'olvi-1', 'directory': '/data/rouhiainen', 'size': '547G', 'min_age': 90},
		{'host': 'olvi-1', 'directory': '/data/s_setup', 'size': '529G', 'min_age': 90},
		{'host': 'olvi-1', 'directory': '/data/yguo', 'size': '502G', 'min_age': 90},
		{'host': 'olvi-1', 'directory': '/data/linbo', 'size': '492G', 'min_age': 90},
		{'host': 'olvi-1', 'directory': '/data/sungjuncho', 'size': '42G', 'min_age': 90},
		{'host': 'olvi-1', 'directory': '/data/jifan', 'size': '357G', 'min_age': 90},
		{'host': 'olvi-1', 'directory': '/data/zhiqi', 'size': '375G', 'min_age': 90}
	])

	post_data([
		{'host': 'olvi-1', 'directory': '/data/milawang', 'size': '982G', 'min_age': 180},
		{'host': 'olvi-1', 'directory': '/data/yzeng58', 'size': '888G', 'min_age': 180},
		{'host': 'olvi-1', 'directory': '/data/changho', 'size': '195G', 'min_age': 180},
		{'host': 'olvi-1', 'directory': '/data/rouhiainen', 'size': '547G', 'min_age': 180},
		{'host': 'olvi-1', 'directory': '/data/s_setup', 'size': '529G', 'min_age': 180},
		{'host': 'olvi-1', 'directory': '/data/yguo', 'size': '365G', 'min_age': 180},
		{'host': 'olvi-1', 'directory': '/data/linbo', 'size': '492G', 'min_age': 180},
		{'host': 'olvi-1', 'directory': '/data/sungjuncho', 'size': '38G', 'min_age': 180},
		{'host': 'olvi-1', 'directory': '/data/jifan', 'size': '182G', 'min_age': 180},
		{'host': 'olvi-1', 'directory': '/data/zhiqi', 'size': '226G', 'min_age': 180}
	])

	post_data([
		{'host': 'olvi-2', 'directory': '/data/milawang', 'size': '1.7T', 'min_age': 30},
		{'host': 'olvi-2', 'directory': '/data/yzeng58', 'size': '986G', 'min_age': 30},
		{'host': 'olvi-2', 'directory': '/data/changho', 'size': '623G', 'min_age': 30},
		{'host': 'olvi-2', 'directory': '/data/rouhiainen', 'size': '547G', 'min_age': 30},
		{'host': 'olvi-2', 'directory': '/data/s_setup', 'size': '529G', 'min_age': 30},
		{'host': 'olvi-2', 'directory': '/data/yguo', 'size': '502G', 'min_age': 30},
		{'host': 'olvi-2', 'directory': '/data/linbo', 'size': '492G', 'min_age': 30},
		{'host': 'olvi-2', 'directory': '/data/sungjuncho', 'size': '411G', 'min_age': 30},
		{'host': 'olvi-2', 'directory': '/data/jifan', 'size': '357G', 'min_age': 30},
		{'host': 'olvi-2', 'directory': '/data/zhiqi', 'size': '375G', 'min_age': 30}
	])

	post_data([
		{'host': 'olvi-2', 'directory': '/data/milawang', 'size': '1.6T', 'min_age': 90},
		{'host': 'olvi-2', 'directory': '/data/yzeng58', 'size': '958G', 'min_age': 90},
		{'host': 'olvi-2', 'directory': '/data/changho', 'size': '219G', 'min_age': 90},
		{'host': 'olvi-2', 'directory': '/data/rouhiainen', 'size': '547G', 'min_age': 90},
		{'host': 'olvi-2', 'directory': '/data/s_setup', 'size': '529G', 'min_age': 90},
		{'host': 'olvi-2', 'directory': '/data/yguo', 'size': '502G', 'min_age': 90},
		{'host': 'olvi-2', 'directory': '/data/linbo', 'size': '492G', 'min_age': 90},
		{'host': 'olvi-2', 'directory': '/data/sungjuncho', 'size': '42G', 'min_age': 90},
		{'host': 'olvi-2', 'directory': '/data/jifan', 'size': '357G', 'min_age': 90},
		{'host': 'olvi-2', 'directory': '/data/zhiqi', 'size': '375G', 'min_age': 90}
	])

	post_data([
		{'host': 'olvi-2', 'directory': '/data/milawang', 'size': '982G', 'min_age': 180},
		{'host': 'olvi-2', 'directory': '/data/yzeng58', 'size': '888G', 'min_age': 180},
		{'host': 'olvi-2', 'directory': '/data/changho', 'size': '195G', 'min_age': 180},
		{'host': 'olvi-2', 'directory': '/data/rouhiainen', 'size': '547G', 'min_age': 180},
		{'host': 'olvi-2', 'directory': '/data/s_setup', 'size': '529G', 'min_age': 180},
		{'host': 'olvi-2', 'directory': '/data/yguo', 'size': '365G', 'min_age': 180},
		{'host': 'olvi-2', 'directory': '/data/linbo', 'size': '492G', 'min_age': 180},
		{'host': 'olvi-2', 'directory': '/data/sungjuncho', 'size': '38G', 'min_age': 180},
		{'host': 'olvi-2', 'directory': '/data/jifan', 'size': '182G', 'min_age': 180},
		{'host': 'olvi-2', 'directory': '/data/zhiqi', 'size': '226G', 'min_age': 180}
	])
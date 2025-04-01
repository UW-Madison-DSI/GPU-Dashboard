################################################################################
#                                                                              #
#                                   gpu.py                                     #
#                                                                              #
################################################################################
#                                                                              #
#        This is a model for managing gpu information.                         #
#                                                                              #
#        Author(s): Abe Megahed                                                #
#                                                                              #
#        This file is subject to the terms and conditions defined in           #
#        'LICENSE.txt', which is part of this source code distribution.        #
#                                                                              #
################################################################################
#     Copyright (C) 2025, Data Science Institute, University of Wisconsin      #
################################################################################

from models.model import Model

class Gpu(Model):

	#
	# constructor
	#

	def __init__(self, attributes = {}):

		"""
		Creates a new model with the specified attributes.

		Parameters:
			attributes (dict): The model's attributes
		"""

		# set attributes
		#
		self.table = 'gpus'
		self.attributes = attributes;
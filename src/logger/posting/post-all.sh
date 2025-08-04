################################################################################
#                                                                              #
#                                  post-all.sh                                 #
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

python3 post-gpus.py
python3 post-processes.py
python3 post-storage.py
python3 post-historical-storage.py

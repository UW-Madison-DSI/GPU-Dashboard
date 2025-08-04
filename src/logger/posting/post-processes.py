################################################################################
#                                                                              #
#                               post-processes.py                              #
#                                                                              #
################################################################################
#                                                                              #
#        This is a utility for reporting process statistics.                   #
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

def post_processes(processes):
	for process in processes:
		response = requests.post(url + '/processes', data=process)
		print(response)

#
# main
#

if __name__ == '__main__':
	post_processes([
		{'host': 'olvi-1', 'gpu': 2, 'pid': 3707469, 'user': 'sungjun+', 'gpu_memory': 31616, 'percent_cpu': '125', 'percent_memory': '0.3', 'time': '10:36', 'command': 'python run_compute_f1.py --split forget01 --gen_model ./llm_weights/ft_epoch5_lr1e-05_llama3.1-8b_fu'},
		{'host': 'olvi-1', 'gpu': 3, 'pid': 3707470, 'user': 'sungjun+', 'gpu_memory': 31616, 'percent_cpu': '115', 'percent_memory': '0.3', 'time': '10:36', 'command': 'python run_compute_f1.py --split forget01 --gen_model ./llm_weights/ft_epoch5_lr1e-05_llama3.1-8b_fu'},
		{'host': 'olvi-1', 'gpu': 4, 'pid': 3560618, 'user': 'clo36', 'gpu_memory': 684, 'percent_cpu': '117', 'percent_memory': '0.1', 'time': '38:09', 'command': '/usr/bin/ollama runner --model /root/.ollama/models/blobs/sha256-970aa74c0a90ef7482477cf803618e776e1'},
		{'host': 'olvi-1', 'gpu': 4, 'pid': 3707471, 'user': 'sungjun+', 'gpu_memory': 31616, 'percent_cpu': '126', 'percent_memory': '0.3', 'time': '10:36', 'command': 'python run_compute_f1.py --split forget01 --gen_model ./llm_weights/ft_epoch5_lr1e-05_llama3.1-8b_fu'},
		{'host': 'olvi-1', 'gpu': 5, 'pid': 1763501, 'user': 'clo36', 'gpu_memory': 1522, 'percent_cpu': '23.8', 'percent_memory': '2.8', 'time': '7', 'command': 'days text-embeddings-router --json-output'}
	])
	post_processes([
		{'host': 'olvi-2', 'gpu': 3, 'pid': 2087172, 'user': 'clo36', 'gpu_memory': 1584, 'percent_cpu': '0.9', 'percent_memory': '2.9', 'time': '04:32:35', 'command': 'text-embeddings-router --json-output'},
		{'host': 'olvi-2', 'gpu': 4, 'pid': 2604716, 'user': 'sungjun+', 'gpu_memory': 15920, 'percent_cpu': '99.9', 'percent_memory': '0.3', 'time': '40:15', 'command': 'python -u run_taqa.py --model_id meta-llama/Llama-3.1-8B --layer_id 6 --alpha 0.0 --steer_year 2021'},
		{'host': 'olvi-2', 'gpu': 4, 'pid': 2719022, 'user': 'sungjun+', 'gpu_memory': 15908, 'percent_cpu': '102', 'percent_memory': '0.3', 'time': '00:42', 'command': 'python -u run_taqa.py --model_id meta-llama/Llama-3.1-8B --layer_id 6 --alpha 0.0 --steer_year 2022'},
		{'host': 'olvi-2', 'gpu': 5, 'pid': 2604718, 'user': 'sungjun+', 'gpu_memory': 15920, 'percent_cpu': '100', 'percent_memory': '0.3', 'time': '40:15', 'command': 'python -u run_taqa.py --model_id meta-llama/Llama-3.1-8B --layer_id 6 --alpha 1.0 --steer_year 2021'},
		{'host': 'olvi-2', 'gpu': 5, 'pid': 2719024, 'user': 'sungjun+', 'gpu_memory': 15918, 'percent_cpu': '101', 'percent_memory': '0.3', 'time': '00:42', 'command': 'python -u run_taqa.py --model_id meta-llama/Llama-3.1-8B --layer_id 6 --alpha 1.0 --steer_year 2022'},
		{'host': 'olvi-2', 'gpu': 6, 'pid': 2604720, 'user': 'sungjun+', 'gpu_memory': 15920, 'percent_cpu': '100', 'percent_memory': '0.3', 'time': '40:15', 'command': 'python -u run_taqa.py --model_id meta-llama/Llama-3.1-8B --layer_id 6 --alpha 2.5 --steer_year 2021'},
		{'host': 'olvi-2', 'gpu': 6, 'pid': 2719026, 'user': 'sungjun+', 'gpu_memory': 15902, 'percent_cpu': '97.5', 'percent_memory': '0.3', 'time': '00:42', 'command': 'python -u run_taqa.py --model_id meta-llama/Llama-3.1-8B --layer_id 6 --alpha 2.5 --steer_year 2022'},
		{'host': 'olvi-2', 'gpu': 7, 'pid': 2719028, 'user': 'sungjun+', 'gpu_memory': 15910, 'percent_cpu': '101', 'percent_memory': '0.3', 'time': '00:42', 'command': 'python -u run_taqa.py --model_id meta-llama/Llama-3.1-8B --layer_id 6 --alpha 5.0 --steer_year 2022'}
	])

/******************************************************************************\
|                                                                              |
|                             gpu-memory-chart.js                              |
|                                                                              |
|******************************************************************************|
|                                                                              |
|        This is a bar chart for displaying gpu usage statistics.              |
|                                                                              |
|        Author(s): Abe Megahed                                                |
|                                                                              |
|        This file is subject to the terms and conditions defined in           |
|        'LICENSE.md', which is part of this source code distribution.         |
|                                                                              |
|******************************************************************************|
|     Copyright (C) 2025, Data Science Institute, University of Wisconsin      |
\******************************************************************************/

class GpuMemoryChart {

	//
	// methods
	//

	constructor(attributes) {

		// set attributes
		//
		this.title = attributes.title;
		this.element = attributes.element;
		this.data = attributes.data;
		this.num_gpus = 8;
		this.gpu_memory = 40;
		this.users = this.getUsers(this.data);

		// show chart
		//
		this.render();
		$(window).on('resize', () => {
			this.render();
		});
	}

	//
	// getting methods
	//

	getUserNames(data) {
		let names = [];
		for (let i = 0; i < data.length; i++) {
			let name = data[i].user;
			if (!names.includes(name)) {
				names.push(name);
			}
		}
		return names;
	}

	getUsers(data) {
		let names = this.getUserNames(data);
		let users = [];
		for (let i = 0; i < names.length; i++) {
			let name = names[i];
			users.push(this.getUser(name, data));
		}
		return users;
	}

	getGpuNames() {
		let names = [];
		for (let i = 0; i < this.num_gpus; i++) {
			names.push('GPU' + i);
		}
		return names;
	}

	getGpuMemoriesByUser(name, data) {
		let memories = [];
		for (let i = 0; i < this.num_gpus; i++) {
			memories.push(this.getGpuMemoryByUser(i, name, data))
		}
		return memories;
	}

	getGpuMemoryByUser(index, name, data) {
		let memory = 0;
		for (let i = 0; i < data.length; i++) {
			let gpu = data[i];
			if (gpu.user == name && gpu.gpu == index) {
				memory += gpu.gpu_memory / 1000;
			}
		}
		return memory;
	}

	getLabels(values) {
		let labels = [];
		for (let i = 0; i < values.length; i++) {
			let value = values[i];
			if (value) {
				labels.push(Math.trunc(value) + ' GB');
			} else {
				labels.push('');
			}
		}
		return labels;
	}

	getUser(name, data) {
		let names = this.getGpuNames();
		let values = this.getGpuMemoriesByUser(name, data);
		let labels = this.getLabels(values);

		return {
			x: names,
			y: values,
			name: name,
			type: 'bar',
			// text: labels,
			// textposition: 'outside'
		};
	}

	//
	// rendering methods
	//

	render() {
		let layout = {
			title: this.title,
			showlegend: true,
			barmode: 'stack',
			width: $(this.element).width(),
			xaxis: {
				title: {
					text: 'GPU'
				}
			},
			yaxis: {
				title: {
					text: 'GPU Memory (GB)'
				},
				range: [0, this.gpu_memory]
			}
		};

		let config = {
			displayModeBar: false
		}

		Plotly.newPlot(this.element, this.users, layout, config);
	}
}
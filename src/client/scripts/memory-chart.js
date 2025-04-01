/******************************************************************************\
|                                                                              |
|                               memory-chart.js                                |
|                                                                              |
|******************************************************************************|
|                                                                              |
|        This is a bar chart for displaying memory usage statistics.           |
|                                                                              |
|        Author(s): Abe Megahed                                                |
|                                                                              |
|        This file is subject to the terms and conditions defined in           |
|        'LICENSE.md', which is part of this source code distribution.         |
|                                                                              |
|******************************************************************************|
|     Copyright (C) 2025, Data Science Institute, University of Wisconsin      |
\******************************************************************************/

class MemoryChart {

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
		this.users = this.getUsers(this.data);

		// show chart
		//
		this.render();
		$(window).on('resize', () => {
			this.render();
		});
	}

	//
	// fetching methods
	//

	update() {
		$.ajax({
			url: this.server + '/gpus/latest?host=' + this.host,
			type: 'GET',
			crossDomain: true,
			headers: {
				"Access-Control-Allow-Origin": "*"
			},

			// callbacks
			//
			success: (data) => {
				this.users = this.getUsers(data);
				this.render();
			}
		});
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

	getGpuNames() {
		let names = [];
		for (let i = 0; i < this.num_gpus; i++) {
			names.push('GPU' + i);
		}
		return names;
	}

	getMemoriesByUser(name, data) {
		let memories = [];
		for (let i = 0; i < this.num_gpus; i++) {
			memories.push(this.getMemoryByUser(i, name, data))
		}
		return memories;
	}

	getMemoryByUser(index, name, data) {
		let memory = 0;
		for (let i = 0; i < data.length; i++) {
			let gpu = data[i];
			if (gpu.user == name && gpu.gpu == index) {
				memory += gpu.percent_memory * 100;
			}
		}
		return memory;
	}

	getUser(name, data) {
		return {
			x: this.getGpuNames(),
			y: this.getMemoriesByUser(name, data),
			name: name,
			type: 'bar'
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
					text: 'Memory (%)'
				},
				// range: [0, 100]
			}
		};

		let config = {
			displayModeBar: false
		}

		Plotly.newPlot(this.element, this.users, layout, config);
	}
}
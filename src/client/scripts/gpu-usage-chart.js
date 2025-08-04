/******************************************************************************\
|                                                                              |
|                              gpu-usage-chart.js                              |
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

class GpuUsageChart {

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
	// getting methods
	//

	getUsers() {
		let names = this.getUserNames();
		let gpus = this.getGpuCountByUsers(names);
		let colors = this.getColors(gpus);
		let labels = this.getLabels(gpus);

		return [{
			x: names,
			y: gpus,
			type: 'bar',
			marker: {
				color: colors
			},
			text: labels,
			textposition: 'outside'
		}];
	}

	getUserNames() {
		let names = [];
		for (let i = 0; i < this.data.length; i++) {
			let name = this.data[i].user;
			if (!names.includes(name)) {
				names.push(name);
			}
		}
		return names;
	}

	getGpuCountByUsers(names) {
		let counts = []
		for (let i = 0; i < names.length; i++) {
			let name = names[i];
			counts.push(this.getGpuCountByUser(name));
		}
		return counts;
	}

	getGpuCountByUser(name) {
		let count = 0;
		for (let gpu = 0; gpu < this.num_gpus; gpu++) {
			if (this.isUsingGpu(name, gpu)) {
				count++;
			}
		}

		return count;
	}

	isUsingGpu(name, gpu) {
		for (let i = 0; i < this.data.length; i++) {
			let item = this.data[i];
			if (item.user == name && item.gpu == gpu) {
				return true;
			}
		}
		return false;
	}

	getColors(values) {
		let colors = []
		for (let i = 0; i < values.length; i++) {
			colors.push(this.getColor(values[i]));
		}
		return colors;
	}

	getColor(value) {
		let high = 8;
		let low = 0;
		let t = (value - low) / (high - low);
		let highColor = [255, 63, 63];
		let midColor = [63, 192, 63];
		let lowColor = [63, 127, 192];
		let r, g, b;

		if (t > 0.5) {
			t = (t - 0.5) * 2;
			r = midColor[0] * (1 - t) + highColor[0] * t;
			g = midColor[1] * (1 - t) + highColor[1] * t;
			b = midColor[2] * (1 - t) + highColor[2] * t;
		} else {
			t = t * 2;
			r = lowColor[0] * (1 - t) + midColor[0] * t;
			g = lowColor[1] * (1 - t) + midColor[1] * t;
			b = lowColor[2] * (1 - t) + midColor[2] * t;
		}

		return 'rgb(' + r + ',' + g + ',' + b + ')';
	}

	getLabels(values) {
		let labels = [];
		for (let i = 0; i < values.length; i++) {
			let value = values[i];
			labels.push(value + ' GPU' + (value != 1? 's' : ''));
		}
		return labels;
	}

	//
	// rendering methods
	//

	render() {
		let layout = {
			title: this.title,
			showlegend: false,
			width: $(this.element).width(),
			xaxis: {
				title: {
					text: 'User'
				}
			},
			yaxis: {
				title: {
					text: 'Number of GPUs'
				},
				range: [0, 8]
			}
		};

		let config = {
			displayModeBar: false
		}

		Plotly.newPlot(this.element, this.users, layout, config);
	}
}
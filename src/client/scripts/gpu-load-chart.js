/******************************************************************************\
|                                                                              |
|                              gpu-load-chart.js                               |
|                                                                              |
|******************************************************************************|
|                                                                              |
|        This is a bar chart for displaying gpu load statistics.               |
|                                                                              |
|        Author(s): Abe Megahed                                                |
|                                                                              |
|        This file is subject to the terms and conditions defined in           |
|        'LICENSE.md', which is part of this source code distribution.         |
|                                                                              |
|******************************************************************************|
|     Copyright (C) 2025, Data Science Institute, University of Wisconsin      |
\******************************************************************************/

class GpuLoadChart {

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
		this.loads = this.getLoads(this.data);

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

	getLoads() {
		let names = this.getGpuNames();
		let loads = this.getGpuLoads();
		let colors = this.getGpuColors(loads);

		return [{
			x: names,
			y: loads,
			marker: {
				color: colors
			},
			type: 'bar'
		}];
	}

	getGpuNames() {
		let names = [];
		for (let i = 0; i < this.num_gpus; i++) {
			names.push('GPU' + i);
		}
		return names;
	}

	getGpuLoads() {
		let loads = []
		for (let i = 0; i < this.num_gpus; i++) {
			loads.push(this.getLoadByGpu(i));
		}
		return loads;
	}

	getGpuColors(loads) {
		let colors = []
		for (let i = 0; i < loads.length; i++) {
			colors.push(this.getGpuColor(loads[i]));
		}
		return colors;
	}

	getGpuColor(load) {
		let high = 100;
		let low = 0;
		let t = (load - low) / (high - low);
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

	getLoadByGpu(index) {
		for (let i = 0; i < this.data.length; i++) {
			let gpu = this.data[i];
			if (gpu.gpu == index) {
				return gpu.gpu_util
			}
		}
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
					text: 'GPU'
				}
			},
			yaxis: {
				title: {
					text: 'Load (%)'
				},
				range: [0, 100]
			}
		};

		let config = {
			displayModeBar: false
		}

		Plotly.newPlot(this.element, this.loads, layout, config);
	}
}
/******************************************************************************\
|                                                                              |
|                              gpu-temp-chart.js                               |
|                                                                              |
|******************************************************************************|
|                                                                              |
|        This is a bar chart for displaying gpu temp statistics.               |
|                                                                              |
|        Author(s): Abe Megahed                                                |
|                                                                              |
|        This file is subject to the terms and conditions defined in           |
|        'LICENSE.md', which is part of this source code distribution.         |
|                                                                              |
|******************************************************************************|
|     Copyright (C) 2025, Data Science Institute, University of Wisconsin      |
\******************************************************************************/

class GpuTempChart {

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
		this.temps = this.getTemps(this.data);

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

	getTemps() {
		let names = this.getGpuNames();
		let temps = this.getGpuTemps();
		let colors = this.getGpuColors(temps);

		return [{
			x: names,
			y: temps,
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

	getGpuTemps() {
		let temps = []
		for (let i = 0; i < this.num_gpus; i++) {
			temps.push(this.getTempByGpu(i));
		}
		return temps;
	}

	getGpuColors(temps) {
		let colors = []
		for (let i = 0; i < temps.length; i++) {
			colors.push(this.getGpuColor(temps[i]));
		}
		return colors;
	}

	getGpuColor(temp) {
		let high = 50;
		let low = 0;
		let t = (temp - low) / (high - low);
		let highColor = [255, 0, 0];
		let midColor = [0, 255, 0];
		let lowColor = [0, 0, 255];
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

	getTempByGpu(index) {
		for (let i = 0; i < this.data.length; i++) {
			let gpu = this.data[i];
			if (gpu.gpu == index) {
				return gpu.temp
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
					text: 'Temp (C)'
				},
				range: [0, 50]
			}
		};

		let config = {
			displayModeBar: false
		}

		Plotly.newPlot(this.element, this.temps, layout, config);
	}
}
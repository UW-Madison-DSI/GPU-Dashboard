/******************************************************************************\
|                                                                              |
|                             gpu-power-chart.js                               |
|                                                                              |
|******************************************************************************|
|                                                                              |
|        This is a bar chart for displaying gpu power statistics.               |
|                                                                              |
|        Author(s): Abe Megahed                                                |
|                                                                              |
|        This file is subject to the terms and conditions defined in           |
|        'LICENSE.md', which is part of this source code distribution.         |
|                                                                              |
|******************************************************************************|
|     Copyright (C) 2025, Data Science Institute, University of Wisconsin      |
\******************************************************************************/

class GpuPowerChart {

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
		this.powers = this.getPowers(this.data);

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

	getPowers() {
		let names = this.getGpuNames();
		let powers = this.getGpuPowers();
		let colors = this.getGpuColors(powers);

		return [{
			x: names,
			y: powers,
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

	getGpuPowers() {
		let powers = []
		for (let i = 0; i < this.num_gpus; i++) {
			powers.push(this.getPowerByGpu(i));
		}
		return powers;
	}

	getGpuColors(powers) {
		let colors = []
		for (let i = 0; i < powers.length; i++) {
			colors.push(this.getGpuColor(powers[i]));
		}
		return colors;
	}

	getGpuColor(power) {
		let high = 250;
		let low = 0;
		let t = (power - low) / (high - low);
		let highColor = [127, 127, 255];
		let midColor = [127, 127, 192];
		let lowColor = [127, 127, 127];
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

	getPowerByGpu(index) {
		for (let i = 0; i < this.data.length; i++) {
			let gpu = this.data[i];
			if (gpu.gpu == index) {
				return gpu.power
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
					text: 'Power (W)'
				},
				range: [0, 250]
			}
		};

		let config = {
			displayModeBar: false
		}

		Plotly.newPlot(this.element, this.powers, layout, config);
	}
}
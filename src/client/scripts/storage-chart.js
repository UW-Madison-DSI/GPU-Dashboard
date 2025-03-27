/******************************************************************************\
|                                                                              |
|                               storage-chart.js                               |
|                                                                              |
|******************************************************************************|
|                                                                              |
|        This is a bar chart for displaying storage usage statistics.          |
|                                                                              |
|        Author(s): Abe Megahed                                                |
|                                                                              |
|        This file is subject to the terms and conditions defined in           |
|        'LICENSE.md', which is part of this source code distribution.         |
|                                                                              |
|******************************************************************************|
|     Copyright (C) 2025, Data Science Institute, University of Wisconsin      |
\******************************************************************************/

class StorageChart {

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
		// this.directories = this.getDirectories(this.data);
		this.show_other = true;

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

	getDirectoryNames(data) {
		let dirnames = [];
		for (let i = 0; i < data.length; i++) {
			let dirname = data[i].directory;
			if (!dirnames.includes(dirname)) {
				dirnames.push(dirname);
			}
		}
		if (this.show_other) {
			dirnames.push('other');
		}
		return dirnames;
	}

	getStoragePercentages(data) {
		let dirnames = this.getDirectoryNames(data);
		let percentages = [];
		let total = 0;
		for (let i = 0; i < data.length; i++) {
			let percentage = 0;
			let amount = data[i].amount;
			if (amount.includes('T')) {
				percentage = parseFloat(amount.replace('T', '')) / 15 * 100;
			}
			if (amount.includes('G')) {
				percentage = parseFloat(amount.replace('G', '')) / 15000 * 100;
			}
			if (amount.includes('M')) {
				percentage = parseFloat(amount.replace('M', '')) / 15000000 * 100;
			}
			total += percentage;
			percentages.push(percentage);
		}
		if (this.show_other) {
			percentages.push(100 - total);
		}
		return percentages;
	}

	getStorageAmounts(data) {
		let dirnames = this.getDirectoryNames(data);
		let amounts = [];
		let total = 0;
		for (let i = 0; i < data.length; i++) {
			let storage = 0;
			let amount = data[i].amount;
			if (amount.includes('T')) {
				storage = parseFloat(amount.replace('T', ''));
			}
			if (amount.includes('G')) {
				storage = parseFloat(amount.replace('G', '')) / 1000;
			}
			if (amount.includes('M')) {
				storage = parseFloat(amount.replace('M', '')) / 1000000;
			}
			total += storage;
			amounts.push(storage);
		}
		if (this.show_other) {
			amounts.push(14 - total);
		}
		return amounts;
	}

	//
	// rendering methods
	//

	render() {
		const data = [{
			labels: this.getDirectoryNames(this.data),
			values: this.getStorageAmounts(this.data),
			type: 'pie',
			hovertemplate: '%{label}<br />%{value} TB<br />(%{percent})<extra></extra>'
		}];

		let layout = {
			title: this.title,
			showlegend: true
		}

		let config = {
			displayModeBar: false
		}

		Plotly.newPlot(this.element, data, layout, config);
	}
}
/******************************************************************************\
|                                                                              |
|                                    main.js                                   |
|                                                                              |
|******************************************************************************|
|                                                                              |
|        This is the main entry point for the dashboard application.           |
|                                                                              |
|        Author(s): Abe Megahed                                                |
|                                                                              |
|        This file is subject to the terms and conditions defined in           |
|        'LICENSE.md', which is part of this source code distribution.         |
|                                                                              |
|******************************************************************************|
|     Copyright (C) 2025, Data Science Institute, University of Wisconsin      |
\******************************************************************************/

//
// globals
//

// let server = 'http://localhost:5000';
let server = 'https://olvi-dashboard-api.services.dsi.wisc.edu';

// allow cross domain requests
//
$.support.cors = true;

//
// methods
//

function showDate(element, date) {
	let timeStr = date.toLocaleTimeString({
		timezone: 'America/Chicago'
	});
	let dateStr = date.toLocaleDateString();
	$(element).find('.date').text(timeStr + ' on ' + dateStr);
	$(element).show();
}

//
// getting methods
//

function getDataByHost(data, host) {
	let items = [];
	for (let i = 0; i < data.length; i++) {
		let item = data[i];
		if (item.host == host) {
			items.push(item);
		}
	}
	return items;
}

function getTheme() {
	let className = $('#theme i').attr('class');
	switch (className) {
		case 'fa fa-paintbrush':
			return 'auto';
		case 'fa fa-sun':
			return 'light';
		case 'fa fa-moon':
			return 'dark';
	}
}

function getNextTheme(theme) {
	switch (theme) {
		case 'auto':
			return 'light';
		case 'light':
			return 'dark';
		case 'dark':
			return 'auto';
	}
}

//
// setting methods
//

function setTheme(theme) {
	switch (theme) {
		case 'auto':
			$('button#theme i').attr('class', 'fa fa-paintbrush');
			$('body').removeClass('light').removeClass('dark');
			break;
		case 'light':
			$('button#theme i').attr('class', 'fa fa-sun');
			$('body').removeClass('dark').addClass('light');
			break;
		case 'dark':
			$('button#theme i').attr('class', 'fa fa-moon');
			$('body').removeClass('light').addClass('dark');
			break;
	}
	localStorage.setItem('theme', theme);
}

//
// fetching methods
//

function fetchGpuData(options) {

	// fetch gpu data
	//
	$.ajax({
		url: server + '/gpus/latest',
		type: 'GET',
		crossDomain: true,
		headers: {
			"Access-Control-Allow-Origin": "*"
		},

		// callbacks
		//
		success: options.success
	});
}

function fetchStorageData(options) {

	// fetch gpu data
	//
	$.ajax({
		url: server + '/storage/latest',
		type: 'GET',
		crossDomain: true,
		headers: {
			"Access-Control-Allow-Origin": "*"
		},

		// callbacks
		//
		success: options.success
	});
}

//
// rendering methods
//

function showGpuCharts(data) {
	let olvi1Data = getDataByHost(data, 'olvi-1');
	let olvi2Data = getDataByHost(data, 'olvi-2');

	// show charts
	//
	let olvi1GpuChart = new GpuChart({
		title: 'Olvi-1 GPU Memory',
		element: $('#olvi-1-gpu-memory .chart')[0],
		data: olvi1Data
	});
	let olvi2GpuChart = new GpuChart({
		title: 'Olvi-2 GPU Memory',
		element: $('#olvi-2-gpu-memory .chart')[0],
		data: olvi2Data
	});

	// show dates
	//
	if (olvi1Data.length > 0) {
		let date = new Date(olvi1Data[0].created_at + 'Z');
		this.showDate($('#olvi-1-gpu-memory .updated'), date);
	}
	if (olvi2Data.length > 0) {
		let date = new Date(olvi2Data[0].created_at + 'Z');
		this.showDate($('#olvi-2-gpu-memory .updated'), date);
	}
}

function showCpuCharts(data) {
	let olvi1Data = getDataByHost(data, 'olvi-1');
	let olvi2Data = getDataByHost(data, 'olvi-2');

	// show charts
	//
	let olvi1CpuChart = new CpuChart({
		title: 'Olvi-1 CPU Load',
		element: $('#olvi-1-cpu-load .chart')[0],
		data: olvi1Data
	});
	let olvi2CpuChart = new CpuChart({
		title: 'Olvi-2 CPU Load',
		element: $('#olvi-2-cpu-load .chart')[0],
		data: olvi2Data
	});

	// show dates
	//
	if (olvi1Data.length > 0) {
		let date = new Date(olvi1Data[0].created_at + 'Z');
		this.showDate($('#olvi-1-cpu-load .updated'), date);
	}
	if (olvi2Data.length > 0) {
		let date = new Date(olvi2Data[0].created_at + 'Z');
		this.showDate($('#olvi-2-cpu-load .updated'), date);
	}
}

function showMemoryCharts(data) {
	let olvi1Data = getDataByHost(data, 'olvi-1');
	let olvi2Data = getDataByHost(data, 'olvi-2');

	// show charts
	//
	let olvi1MemoryChart = new MemoryChart({
		title: 'Olvi-1 Memory',
		element: $('#olvi-1-memory .chart')[0],
		data: olvi1Data
	});
	let olvi2MemoryChart = new MemoryChart({
		title: 'Olvi-2 Memory',
		element: $('#olvi-2-memory .chart')[0],
		data: olvi2Data
	});

	// show dates
	//
	if (olvi1Data.length > 0) {
		let date = new Date(olvi1Data[0].created_at + 'Z');
		this.showDate($('#olvi-1-memory .updated'), date);
	}
	if (olvi2Data.length > 0) {
		let date = new Date(olvi2Data[0].created_at + 'Z');
		this.showDate($('#olvi-2-memory .updated'), date);
	}
}

function showStorageCharts(data) {
	let olvi1Data = getDataByHost(data, 'olvi-1');
	let olvi2Data = getDataByHost(data, 'olvi-2');

	// storage charts
	//
	let olvi1StorageChart = new StorageChart({
		title: 'Olvi-1 Storage',
		element: $('#olvi-1-storage .chart')[0],
		data: olvi1Data
	});
	let olvi2StorageChart = new StorageChart({
		title: 'Olvi-2 Storage',
		element: $('#olvi-2-storage .chart')[0],
		data: olvi2Data
	});

	// show dates
	//
	if (olvi1Data.length > 0) {
		let date = new Date(olvi1Data[0].created_at + 'Z');
		this.showDate($('#olvi-1-storage .updated'), date);
	}
	if (olvi2Data.length > 0) {
		let date = new Date(olvi2Data[0].created_at + 'Z');
		this.showDate($('#olvi-2-storage .updated'), date);
	}
}

//
// main
//

window.onload = function() {

	// set initial theme
	//
	let theme = localStorage.getItem('theme');
	if (theme) {
		setTheme(theme);
	}

	// fetch and show data
	//
	this.fetchGpuData({

		// callbacks
		//
		success: (data) => {
			showGpuCharts(data);
			showCpuCharts(data);
			showMemoryCharts(data);

			this.fetchStorageData({

				// callbacks
				//
				success: (data) => {
					showStorageCharts(data);
				}
			});
		}
	});

	// set tab callbacks
	//
	$('a#gpu').click(() => {
		let url = window.location.href;
		let baseUrl = url.substr(0, url.indexOf('#'));
		history.replaceState(null, null, baseUrl);
	});
	$('a#cpu').click(() => {
		window.location.hash = 'cpu';
	});
	$('a#memory').click(() => {
		window.location.hash = 'memory';
	});
	$('a#storage').click(() => {
		window.location.hash = 'storage';
	});

	// set initial tab
	//
	let activeTab = window.location.hash.replace('#', '');
	if (activeTab) {
		$('a#'+ activeTab).tab('show');
	}

	// button callback
	//
	$('button#theme').click(() => {
		setTheme(getNextTheme(getTheme()));
	});
}
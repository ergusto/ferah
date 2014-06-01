window.ff = window.ff || {};
ff.utils = ff.utils || {};

ff.utils.ajax = (function($) {

	var ajax = {};

	function getJSON(url) {
		return $.ajax({
			type: 'GET',
			dataType: 'json',
			url: url,
		});
	}

	function postJSON(object, url) {
		var data = JSON.stringify(object);
		return $.ajax({
			type: 'POST',
			dataType: 'json',
			url: url,
			data: data,
		});
	}

	function getHTML(url) {
		return $.ajax({
			type: 'GET',
			dataType: 'html',
			url: url,
		});
	}

	ajax.getJSON = getJSON;
	ajax.getHTML = getHTML;

	return ajax;

}(jQuery));
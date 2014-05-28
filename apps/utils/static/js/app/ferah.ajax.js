window.ff = window.ff || {};

ff.ajax = (function($) {

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

	ajax.getJSON = getJSON;

	return ajax;

}(jQuery));
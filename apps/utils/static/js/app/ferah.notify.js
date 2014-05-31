window.ff = window.ff || {};
ff.objects = ff.objects || {};

(function() {

	'use strict';

	var Notify = function() {

	};

	Notify.prototype.render = function(title, options) {
		options = options || {};

		var notification = ff.create('div', ['notification']),
			text = ff.text('fuck yeah!');

		document.body.appendChild(notification);

		window.setTimeout(function() {
			document.body.removeChild(notification);
		}, 1200);

	};

	ff.objects.Notify = Notify

}());
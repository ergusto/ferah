window.ff = window.ff || {};
ff.objects = ff.objects || {};

(function() {

	'use strict';

	var Modal = function() {};

	Modal.prototype.render = function(html, callback) {

		var wrapper = ff.create('div', ['modal-wrapper']),
			modalMainClasses = ['modal', 'col-xs-10', 'col-xs-offset-1', 'col-sm-6', 'col-sm-offset-3', 'col-md-4', 'col-md-offset-4'],
			modalMain = ff.create('div', modalMainClasses);

		modalMain.appendChild(html);
		wrapper.appendChild(modalMain);

		ff.utils.addClass(document.body, 'modal-open');
		document.body.appendChild(wrapper);

		this.modalCount++;

		var closeHandler = function(event) {
			if (event.target !== this) {
				return;
			}
			event.preventDefault();
			self.modalCount--;
			ff.utils.removeClass(document.body, 'modal-open');
			ff.utils.remove(wrapper);
		};

		ff.on(wrapper, 'click', closeHandler, false);
		ff.live('.modal-cancel', 'click', closeHandler, false);

		if (callback && typeof callback === 'function') {
			callback();
		}

	};

	ff.objects.Modal = Modal;

}());
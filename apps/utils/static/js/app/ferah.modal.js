window.ff = window.ff || {};
ff.objects = ff.objects || {};

(function() {

	'use strict';

	var Modal = function() {
		this.modalCount = 0;
	};

	Modal.prototype.render = function(title, html, options) {
		options = options || {};
		var self = this;

		var wrapper = ff.create('div', ['modal-wrapper']),
			modalMainClasses = ['modal', 'col-xs-10', 'col-xs-offset-1', 'col-sm-6', 'col-sm-offset-3', 'col-md-4', 'col-md-offset-4'],
			modalMain = ff.create('div', modalMainClasses),
			modalHeader = ff.create('header', ['box__header']),
			headerTitle = ff.create('h3'),
			headerText = ff.utils.text(title),
			modalBody = ff.create('div', ['modal-body']);

		if (html) {
			modalBody.appendChild(html);
		}

		wrapper.appendChild(modalMain);
		headerTitle.appendChild(headerText);
		modalHeader.appendChild(headerTitle);
		modalMain.appendChild(modalHeader);
		modalMain.appendChild(modalBody);

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

	};

	ff.objects.Modal = Modal;

}());
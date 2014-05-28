window.ff = window.ff || {};

(function() {

	var Modal = function() {
		this.modalCount = 0;
	};

	Modal.prototype.render = function(title, options) {
		options = options || {};
		var self = this;

		var wrapper = document.createElement('div'),
			modalBackdrop = document.createElement('div'),
			modalWrapper = document.createElement('div'),
			modalHeader = document.createElement('header'),
			modalHeaderClose = document.createElement('span'),
			modalHeaderCloseText = document.createTextNode('x'),
			headerTitle = document.createElement('h3'),
			headerText = document.createTextNode('Hello Modal'),
			modalBody = document.createElement('div'),
			modalFooter = document.createElement('footer');

		this.modalCount++;
		ff.addClass(wrapper, 'modal-wrapper');
		ff.addClass(modalWrapper, 'modal');
		ff.addClass(modalHeader, 'modal-header');
		ff.addClass(modalHeaderClose, 'modal-close');
		ff.addClass(modalBody, 'modal-body');
		ff.addClass(modalFooter, 'modal-footer');

		wrapper.appendChild(modalWrapper);
		headerTitle.appendChild(headerText);
		modalHeaderClose.appendChild(modalHeaderCloseText);
		modalHeader.appendChild(modalHeaderClose);
		modalHeader.appendChild(headerTitle);
		modalWrapper.appendChild(modalHeader);
		modalWrapper.appendChild(modalBody);
		modalWrapper.appendChild(modalFooter);

		ff.addClass(document.body, 'modal-open');
		document.body.appendChild(wrapper);

		var closeHandler = function(event) {
			self.modalCount--;
			ff.removeClass(document.body, 'modal-open');
			document.body.removeChild(wrapper);
		};

		modalHeaderClose.addEventListener('click', closeHandler, false);

	};

	ff.Modal = Modal;

}());
window.ff = window.ff || {};

(function() {

	var Modal = function() {
		this.modalCount = 0;
	};

	Modal.prototype.render = function(title, options) {
		options = options || {};
		var self = this;

		var wrapper = ff.create('div', ['modal-wrapper']),
			modalMainClasses = ['modal', 'col-xs-10', 'col-xs-offset-1', 'col-sm-6', 'col-sm-offset-3', 'col-md-4', 'col-md-offset-4'],
			modalMain = ff.create('div', modalMainClasses),
			modalHeader = ff.create('header', ['modal-header']),
			modalHeaderClose = ff.create('span', ['modal-close']),
			headerTitle = ff.create('h3'),
			modalBody = ff.create('div', ['modal-body']),
			modalFooter = ff.create('footer', ['modal-footer']),
			
			modalBodyText = ff.utils.text('Hello body'),
			headerText = ff.utils.text('Hello Modal'),
			modalHeaderCloseText = ff.utils.text('x');

		if (title) {
			headerText = ff.utils.text(title);
		}

		this.modalCount++;

		wrapper.appendChild(modalMain);
		headerTitle.appendChild(headerText);
		modalHeaderClose.appendChild(modalHeaderCloseText);
		modalHeader.appendChild(modalHeaderClose);
		modalHeader.appendChild(headerTitle);
		modalMain.appendChild(modalHeader);
		modalBody.appendChild(modalBodyText);
		modalMain.appendChild(modalBody);
		modalMain.appendChild(modalFooter);

		ff.utils.addClass(document.body, 'modal-open');
		document.body.appendChild(wrapper);

		var closeHandler = function(event) {
			self.modalCount--;
			ff.utils.removeClass(document.body, 'modal-open');
			document.body.removeChild(wrapper);
		};

		modalHeaderClose.addEventListener('click', closeHandler, false);

	};

	ff.Modal = Modal;

}());
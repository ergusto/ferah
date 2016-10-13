window.ff = window.ff || {};
ff.templates = ff.templates || {};
ff.templates.utils = ff.templates.utils || {};

(function() {

	'use strict';

	ff.templates.utils.empty_box = function(title, html) {
		var box = ff.create('div', ['box']),
				boxHeader = ff.create('header', ['box__header']),
		 		boxHeaderTitle = ff.create('h3'),
		 		boxHeaderTitleText = ff.utils.text(title),
				boxBody = ff.create('div', ['box__body']);

		boxHeaderTitle.appendChild(boxHeaderTitleText);
		boxHeader.appendChild(boxHeaderTitle);

		box.appendChild(boxHeader);
		box.appendChild(html);

		return box;
	};

	ff.templates.utils.confirm_delete_object_form = function(url) {

		var csrftoken = ff.utils.csrfcookie(),
			csrfinput = ff.create('input', { 'type': 'hidden', 'name': 'csrfmiddlewaretoken', 'value': csrftoken }),
	 		form = ff.create('form', { 'action': url, 'method': 'post' }),
			boxBody = ff.create('div', ['box__body']),
			bodyParagraph = ff.create('p'),
			bodyParagraphText = ff.utils.text('Are you sure you want to delete this object?'),
			boxFooter = ff.create('div', ['box__footer']),
			btnGroup = ff.create('div', ['btn-group']),
			submit = ff.create('input', ['btn'], { 'type': 'submit', 'value': 'Confirm' }),
			cancel = ff.create('a', ['btn', 'modal-cancel'], { 'href': '#' }),
			cancelText = ff.utils.text('Cancel');

		bodyParagraph.appendChild(bodyParagraphText);
		boxBody.appendChild(bodyParagraph);
		form.appendChild(csrfinput);
		form.appendChild(boxBody);

		cancel.appendChild(cancelText);
		btnGroup.appendChild(submit);
		btnGroup.appendChild(cancel);
		boxFooter.appendChild(btnGroup);
		form.appendChild(boxFooter);

		return form;
				 
	};

}());
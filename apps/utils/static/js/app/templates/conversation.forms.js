window.ff = window.ff || {};
ff.templates = ff.templates || {};
ff.templates.forms = ff.templates.forms || {};

(function() {

	'use strict';

	ff.templates.forms.create_conversation_form = function() {

		var form = ff.create('form', ['clearfix', 'page_form'], { 'id': 'js-conversation-form', 'action': '/conversations/create/', 'method': 'post' }),
			csrftoken = ff.utils.csrfcookie(),
			csrfinput = ff.create('input', { 'type': 'hidden', 'name': 'csrfmiddlewaretoken', 'value': csrftoken }),
			
			formGroup1 = ff.create('div', ['form-group']),
			titleLabel = ff.create('label'),
			titleLabelText = ff.utils.text('Title:'),
			titleInput = ff.create('input', { 'id': 'id_conversation_create_title', 'maxlength': '140', 'name': 'title', 'type': 'text' }),

			formGroup2 = ff.create('div', ['form-group']),
			selectWrapper = ff.create('div', ['select-style']),
			select = ff.create('select', { 'id': 'id_conversation_create_label', 'name': 'label' }),
			defaultOption = ff.create('option', { 'value': '', 'selected': 'selected' }),
			defaultOptionText = ff.utils.text('---------'),
			firstOption = ff.create('option', { 'value': 'blue' }),
			firstOptionText = ff.utils.text('Fergus'),
			secondOption = ff.create('option', { 'value': 'purple' }),
			secondOptionText = ff.utils.text('Farah'),
			
			submitText= ff.utils.text('Submit'),
			submit = ff.create('button', ['btn'], { 'type': 'submit' }),
			formErrors = ff.create('div', { 'id': 'form_errors' });

			form.appendChild(csrfinput);

			titleLabel.appendChild(titleLabelText);
			formGroup1.appendChild(titleLabel);
			formGroup1.appendChild(titleInput);

			form.appendChild(formGroup1);

			defaultOption.appendChild(defaultOptionText);
			firstOption.appendChild(firstOptionText);
			secondOption.appendChild(secondOptionText);

			select.appendChild(defaultOption);
			select.appendChild(firstOption);
			select.appendChild(secondOption);

			selectWrapper.appendChild(select);

			formGroup2.appendChild(selectWrapper);

			form.appendChild(formGroup2);
			submit.appendChild(submitText);
			form.appendChild(submit);
			form.appendChild(formErrors);

			return form;

	};

}());
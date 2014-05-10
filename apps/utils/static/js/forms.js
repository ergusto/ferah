function apply_form_field_error(fieldname, error) {
	var input = $("#id_" + fieldname),
		error_msg = $("<span />").addClass('error').text(error[0]);

	error_msg.insertAfter(input);
}

function apply_form_error(form, error) {
	var div = form.find('#page_form_error'),
		error_msg = $('<span />').addClass('form-error').text(error[0]);

	div.css('display', 'block');
	div.append(error_msg);
}

function clear_form_errors(form) {
	$('#page_form_error').empty();
	$('.error', $(form)).remove();
}
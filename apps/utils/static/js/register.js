$(document).ready(function(){
	$(document).on('submit', '#login_form', function(event) {
		event.preventDefault();
		var form = $(this);
		clear_form_errors(form);
		$.ajax({
			type: form.attr('method'),
			url: form.attr('action'),
			data: form.serialize(),
			success: function(response) {
				if (response.redirect_url) {
					window.location.replace(response.redirect_url);
				} else {
					console.log(response);
				}
			},
			error: function(response, textStatus, jqXHR) {
				var errors = $.parseJSON(response.responseText);
				$.each(errors, function(index, value) {
					if (index === "__all__") {
						apply_form_error(form, value);
					} else {
						apply_form_field_error(index, value);
					}
				});
			}
		});
	});
});
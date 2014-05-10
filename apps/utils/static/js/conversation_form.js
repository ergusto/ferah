$(document).ready(function(){
	$('body').on('submit', '#js-conversation-form', function(event){
		event.preventDefault();
		var form = $(this);
		clear_form_errors(form);
		$.ajax({
			type: form.attr('method'),
			url: form.attr('action'),
   			contentType: 'application/x-www-form-urlencoded;charset=utf-8',
			data: form.serialize(),
			success: function(response) {
				if (response.get_absolute_url) {
					window.location.replace(response.get_absolute_url);
				} else {
					console.log(response);
				}
			},
			error: function(response, textStatus, jqXHR){
				console.log(response);
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
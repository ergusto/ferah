$(document).ready(function(){
	$.ajaxSetup({ 
		beforeSend: function(xhr, settings) {
			function getCookie(name) {
				var cookieValue = null;
				if (document.cookie && document.cookie != '') {
					var cookies = document.cookie.split(';');
					for (var i = 0; i < cookies.length; i++) {
						var cookie = jQuery.trim(cookies[i]);
						if (cookie.substring(0, name.length + 1) == (name + '=')) {
							cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
							break;
						}
					}
				}
				return cookieValue;
			}
			if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
				xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			}
		}
	});
});

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
	var div = form.find('#page_form_error');
	div.empty();
	$('.error', $(form)).remove();
}

(function($) {
	var django_forms = django_forms || {};
	django_forms.forms = {};

	django_forms.forms.opts = {
		create_params: {
			on_form_submit: function($form) { },
		},
	};
	
})(jQuery);
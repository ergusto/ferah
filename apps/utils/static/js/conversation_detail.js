$(document).ready(function(){

	$('body').on('click', '.js-messages-load', function(event){
		event.preventDefault();
		var url = $(this).attr('href');
		var that = this;
		$.ajax({
			type: 'GET',
			dataType: 'json',
			url: url,
			success: function(response) {
				$(that).parent().remove();
				var context = response;
				var source = $('#message_list_template').html();
				var template = Handlebars.compile(source);
				$('#js-messages-list').append(template(context));
				console.log(response);
			},
			error: function(response, textStatus, jqXHR) {
				console.log(response);
				console.log(textStatus);
				console.log(jqXHR);
			}
		});
	});

	$('body').on('submit', '#js-message-form', function(event){
		event.preventDefault();
		var form = $(this);
		clear_form_errors(form);
		$.ajax({
			type: form.attr('method'),
			url: form.attr('action'),
			data: form.serialize(),
			success: function(response) {
				var context = response;
				var source = $('#message_item_template').html();
				var template = Handlebars.compile(source);
				$('#js-messages-list').prepend(template(context));
				$(form).trigger("reset");
			},
			error: function(response, textStatus, jqXHR){
				var errors = $.parseJSON(response.responseText);
				console.log(response);
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

	$(document).on('click', '.js-tag-remove', function(event){
		event.preventDefault();
		var anchor = $(this);
		var title = anchor.parent().text().trim();
		$.ajax({
			url: anchor.attr('href'),
			type: 'POST',
			data: {'title': title},
			dataType: 'json',
			success: function(response) {
				anchor.closest('.tag-list__item').remove();
			},
			error: function(response, textStatus, jqXHR) {
				console.log(response);
				console.log(response);
			}
		});
	});

	$(document).on('submit', '#conversation_tag_form', function(event) {
		event.preventDefault();
		var form = $(this);
		clear_form_errors(form);
		$.ajax({
			url: form.attr('action'),
			type: form.attr('method'),
			dataType: "json",
   			contentType: 'application/x-www-form-urlencoded;charset=utf-8',
			data: form.serialize(),
			success: function(response) {
				var context = response;
				var source = $('#tag_template').html();
				var template = Handlebars.compile(source);
				$('.tags_ul').append(template(context));
				form.find('#id_title').val('');
				console.log(response);
			},
			error: function(response, textStatus, jqXHR) {
				var errors = $.parseJSON(response.responseText);
				console.log(response);
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
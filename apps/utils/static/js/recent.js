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
				$('#js-recent-messages-list').append(template(context));
				console.log(response);
			},
			error: function(response, textStatus, jqXHR) {
				console.log(response);
				console.log(textStatus);
				console.log(jqXHR);
			}
		});
	});
});
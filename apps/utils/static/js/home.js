$(document).ready(function(){

	$('body').on('click', '.js-conversations-load', function(event){
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
				var source = $('#conversation_item_template').html();
				var template = Handlebars.compile(source);
				$('#js-conversations-list').append(template(context));
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
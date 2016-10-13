$(document).ready(function() {
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
				anchor.closest('.tag_list__item').remove();
			},
			error: function(response, textStatus, jqXHR) {
				console.log(response);
				console.log(response);
			}
		});
	});
});
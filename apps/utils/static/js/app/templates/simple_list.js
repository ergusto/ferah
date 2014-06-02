window.ff = window.ff || {};
ff.templates = ff.templates || {};

(function() {

	ff.templates.simple_list = function(response) {
		var wrapper = ff.create('div');

		response.results.forEach(function(result, i) {
			
			var li = ff.create('li');
			var anchor = ff.create('a', ['item_title'], { 'href': result.get_absolute_url });
			var title = ff.utils.text(result.title);
			
			if (result.label) {
				ff.utils.addClass(li, result.label);
			}

			anchor.appendChild(title);
			li.appendChild(anchor);
			wrapper.appendChild(li);

		});

		if (response.next) {
			var li = ff.create('li', ['load-more']);
			var anchor = ff.create('a', ['btn', 'btn-large', 'btn-block'], { 'href': response.next, 'id': 'js-conversations-load' });
			var text = ff.utils.text('Load more');

			anchor.appendChild(text);
			li.appendChild(anchor);
			wrapper.appendChild(li);

			next = response.next;
		}
		return wrapper
	}

}());
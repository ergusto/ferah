window.ff = window.ff || {};
ff.pages = ff.pages || {};

ff.pages.conversation_list = (function() {

	var conversation_list = {},
		next = '', 
		element = ff.qs('#ui-conversations');

	function init() {
		loadConversations();
		primeEventListeners();
	}

	function render(response) {
		
		var wrapper = document.createElement('div');

		response.results.forEach(function(result, i) {
			
			var li = ff.create('li');
			var anchor = ff.create('a', ['item_title'], { 'href': result.get_absolute_url });
			var title = ff.utils.utils.text(result.title);
			
			if (result.label) {
				ff.utils.utils.addClass(li, result.label);
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
		element.innerHTML += wrapper.innerHTML;

	}

	function loadConversations() {
		if (next.length) {
			var request = ff.ajax.getJSON(next);
		} else {
			var request = ff.ajax.getJSON('/api/conversations/');
		}
		request.done(function(response) {
			render(response);
		});
	}

	function primeEventListeners() {
		ff.live('#js-conversations-load', 'click', function(event){
			event.preventDefault();
			$(this).parent().remove();
			loadConversations();
		});
	}

	conversation_list.init = init;

	return conversation_list;

}());
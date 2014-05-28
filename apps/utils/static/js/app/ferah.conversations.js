window.ff = window.ff || {};
ff.components = ff.components || {};

ff.components.conversation_list = (function() {

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
			
			var li = document.createElement('li');
			var anchor = document.createElement('a');
			var title = document.createTextNode(result.title);
			
			if (result.label) {
				ff.addClass(li, result.label);
			}
			ff.addClass(anchor, 'item_title');

			anchor.setAttribute('href', result.get_absolute_url);
			anchor.appendChild(title);
			li.appendChild(anchor);
			wrapper.appendChild(li);

		});

		if (response.next) {
			var li = document.createElement('li');
			var anchor = document.createElement('a');
			var text = document.createTextNode('Load more');

			ff.addClass(li, 'load-more');
			ff.addClass(anchor, 'btn');
			ff.addClass(anchor, 'btn-large');
			ff.addClass(anchor, 'btn-block');
			anchor.setAttribute('href', response.next);
			anchor.setAttribute('id', 'js-conversations-load');

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
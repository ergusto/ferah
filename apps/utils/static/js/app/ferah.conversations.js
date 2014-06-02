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
		
		var wrapper = ff.templates.simple_list(response.results, response.next);
		element.innerHTML += wrapper.innerHTML;

	}

	function loadConversations() {
		if (next.length) {
			var request = ff.utils.ajax.getJSON(next);
		} else {
			var request = ff.utils.ajax.getJSON('/api/conversations/');
		}
		request.done(function(response) {
			render(response);
		});
	}

	function primeEventListeners() {
		ff.live('#js-conversations-load', 'click', function(event){
			event.preventDefault();
			ff.utils.remove(this.parentNode);
			loadConversations();
		});
	}

	conversation_list.init = init;

	return conversation_list;

}());
window.ferah = window.ferah || {};
ferah.components = ferah.components || {};

ferah.components.conversation_list = (function($, Handlebars) {

	var conversation_list = {},
		items = new Array(), 
		next = '', 
		previous = '', 
		templates = {},
		element = $('#ui-conversations');

	templates.simpleList = '{{#each results}}' +
			'<li class="{{ label }}">' +
			'<a class="item_title" href="{{ get_absolute_url }}">{{ title }}</a>' + 
			'</li>' + 
			'{{/each}}' + 
			'{{#if next}}' +
			'<li class="load-more">' +
			'<a id="js-conversations-load" href="#" class="btn btn-large btn-block">Load more</a>' +
			'</li>' +
			'{{/if}}';

	function init() {
		loadConversations();
		primeEventListeners();
	}

	function loadConversations() {
		if (next.length) {
			var request = ferah.ajax.getJSON(next);
		} else {
			var request = ferah.ajax.getJSON('/api/conversations/');
		}
		request.done(function(response) {
			var context = response;
			var source = templates.simpleList;
			var template = Handlebars.compile(source);
			var html = template(context);
			element.append(html);
			next = response.next;
			console.log(next);
		});
	}

	function primeEventListeners() {
		$(document).on('click', '#js-conversations-load', function(event){
			event.preventDefault();
			$(this).parent().remove();
			loadConversations();
		});
	}

	conversation_list.init = init;

	return conversation_list;

}(jQuery, Handlebars));
window.ff = window.ff || {};

(function() {

	// Dom ready
	ff.ready = function(callback) {
		document.addEventListener('DOMContentLoaded', callback);
	};
	
	// Get element(s) by CSS selector:
	ff.qs = function(selector, scope) {
		return (scope || document).querySelector(selector);
	};
	ff.qsa = function(selector, scope) {
		return (scope || document).querySelectorAll(selector);
	};

	// addEventListener wrapper:
	ff.on = function(target, type, callback, useCapture) {
		target.addEventListener(type, callback, !!useCapture);
	};

	// removeEventListener wrapper:
	ff.off = function(target, type, callback) {
		target.removeEventListener(type, callback);
	};

	// Register events on elements that may or may not exist.
	// ff.live('div a', 'click', funciton(event) {});
	ff.live = (function() {
		var eventRegistry = {};

		function dispatchEvent(event) {
			var targetElement = event.target;

			eventRegistry[event.type].forEach(function(entry) {
				var potentialElements = ff.qsa(entry.selector);
				var hasMatch = Array.prototype.indexOf.call(potentialElements, targetElement) >= 0;

				if (hasMatch) {
					entry.handler.call(targetElement, event);
				}
			});
		}

		return function(selector, event, handler) {
			if (!eventRegistry[event]) {
				eventRegistry[event] = [];
				ff.on(document.documentElement, event, dispatchEvent, true);
			}

			eventRegistry[event].push({
				selector: selector,
				handler: handler
			});
		};
	}());

	// Each implementation. Callback gets element and i
	// params

	ff.each = function(selector, callback) {
		var elements = ff.qsa(selector);
		Array.prototype.forEach.call(elements, callback);
	};

	// Add class
	ff.addClass = function(element, className) {
		if (element.classList) {
			element.classList.add(className);
		} else {
			element.classList += ' ' + className;
		}
	};

	ff.hasClass = function(element, className) {
		if (element.classList) {
			return element.classList.contains(className);
		} else {
			return new RegExp('(^| )' + className + '( |$)', 'gi').test(element.className);
		}
	};

	ff.toggleClass = function(element, className) {
		if (element.classList) {
			element.classList.toggle(className);
		} else {
			var classes = element.className.split(' ');
			var existingIndex = classes.indexOf(className);

			if (existingIndex >= 0) {
				classes.splice(existingIndex, 1);
			} else {
				classes.push(className);
			}

			element.className = classes.join(' ');
		}
	};

}());
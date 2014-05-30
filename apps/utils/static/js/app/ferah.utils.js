window.ff = window.ff || {};
ff.utils = ff.utils || {};

(function() {

	'use strict';

	// Dom ready
	ff.ready = function(callback) {
		document.addEventListener('DOMContentLoaded', callback);
	};
	// Get element by CSS selector:
	ff.qs = function(selector, scope) {
		return (scope || document).querySelector(selector);
	};
	// addEventListener wrapper:
	ff.on = function(target, type, callback, useCapture) {
		target.addEventListener(type, callback, !!useCapture);
	};
	// Register events on elements that may or may not exist.
	// ff.live('div a', 'click', funciton(event) {});
	ff.live = (function() {
		var eventRegistry = {};

		function dispatchEvent(event) {
			var targetElement = event.target;

			eventRegistry[event.type].forEach(function(entry) {
				var potentialElements = ff.utils.qsa(entry.selector);
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
	// Create dom elements. Provide a list of class names
	// and/or an object containing keys/values for attributes.
	ff.create = function(tagName, classList, attributeObject) {
		var element = document.createElement(tagName);
		var classListType = typeof classList;
		if (classList) {
			for (var i = 0; i < classList.length; i++) {
				ff.utils.addClass(element, classList[i]);
			}
		}
		if (attributeObject) {
			for (var property in attributeObject) {
				if (attributeObject.hasOwnProperty(property)) {
					element.setAttribute(property, attributeObject[property]);
				}
			}
		}
		return element;
	};



	// Get elements by CSS selector:
	ff.utils.qsa = function(selector, scope) {
		return (scope || document).querySelectorAll(selector);
	};

	// removeEventListener wrapper:
	ff.utils.off = function(target, type, callback) {
		target.removeEventListener(type, callback);
	};

	// Each implementation. Callback gets element and i
	// params

	ff.utils.each = function(selector, callback) {
		var elements = ff.utils.qsa(selector);
		Array.prototype.forEach.call(elements, callback);
	};

	ff.utils.hasClass = function(element, className) {
		if (element.classList) {
			return element.classList.contains(className);
		} else {
			return new RegExp('(^| )' + className + '( |$)', 'gi').test(element.className);
		}
	};

	ff.utils.removeClass = function(element, className) {
		if (ff.utils.hasClass(element, className)) {
			element.className = element.className.replace(new RegExp("(^|\\s)" + className + "(\\s|$)"), " ").replace(/\s$/, "");
		}
	};

	// Add class
	ff.utils.addClass = function(element, className) {
		if (element.classList) {
			element.classList.add(className);
		} else {
			element.classList += ' ' + className;
		}
	};

	ff.utils.toggleClass = function(element, className) {
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

	ff.utils.text = function(text) {
		return document.createTextNode(text);
	};

}());
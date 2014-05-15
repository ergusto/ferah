;(function($, window, document, undefined) {
	'use strict';

	var pluginName = 'jangoTags',
		defaults = {
			handlebarsTemplate: null,
			appendTo: null,
			prependTo: null,
		};

	function JangoTags(form, settings) {
		this.form = $(form);

		this.settings = settings;
		this._defaults = defaults;
		this._name = pluginName;
		this.init();
	}

	JangoTags.prototype = {

		init: function() {
			this.primeEventListeners();
		},

	};

	$.fn[ pluginName ] = function(options) {
		return this.each(function() {
			var settings = $.extend( {}, defaults, options);
			if ( !$.data( this, "plugin_" + pluginName ) ) {
				$.data( this, "plugin_" + pluginName, new JangoTags(this, settings) );
			}
		}, options);
	};

})(jQuery, window, document);
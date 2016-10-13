from django import template

register = template.Library()

@register.filter
def widget_type(obj):
	return obj.__class__.__name__
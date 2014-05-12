from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from braces.forms import UserKwargModelFormMixin
from django.template.defaultfilters import slugify

from apps.conversations.models import Conversation

from models import Tag

class SimpleTagForm(forms.ModelForm):

	class Meta:
		model = Tag
		fields = ('title',)

	def __init__(self, *args, **kwargs):
		super(SimpleTagForm, self).__init__(*args, **kwargs)
		self.fields['title'].label = 'Tag text'
		self.fields['title'].help_text = 'Enter tags separated by a comma.'

class TagForm(forms.ModelForm):

	class Meta:
		model = Tag
		fields = ('title',)

	def __init__(self, *args, **kwargs):
		super(TagForm, self).__init__(*args, **kwargs)
		self.fields['title'].label = 'Tag text'
		self.fields['title'].help_text = 'Enter tags separated by a comma.'

	def clean_title(self):
		title = self.cleaned_data['title']
		slug = slugify(title)
		if len(slug) == 0:
			raise forms.ValidationError("Please enter a valid tag title.")
		try:
			convo = Conversation.objects.get(slug=slug)
		except Conversation.DoesNotExist:
			return title
		else:
			if self.instance and convo == self.instance:
				return title
			raise forms.ValidationError("A conversation with that title already exists.")
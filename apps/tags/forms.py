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
		if len(title) >= 50:
			raise forms.ValidationError("Tag title must be 50 characters or fewer.")
		slug = slugify(title)
		if len(slug) == 0:
			raise forms.ValidationError("Please enter a valid tag title.")
		return title
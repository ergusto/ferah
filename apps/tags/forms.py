from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from braces.forms import UserKwargModelFormMixin
from django.template.defaultfilters import slugify

from apps.conversations.models import Conversation

from models import Tag

class TagForm(forms.ModelForm):

	class Meta:
		model = Tag
		fields = ('title',)

	def __init__(self, *args, **kwargs):
		self.conversation = kwargs.pop('conversation', None)
		super(TagForm, self).__init__(*args, **kwargs)
		self.fields['title'].label = 'Tag text'
		self.fields['title'].help_text = 'Enter tags separated by a comma.'

	def clean_title(self):
		title = self.cleaned_data['title']
		if len(title) > 30:
			raise forms.ValidationError("Tag title must be 30 characters or fewer.")
		slug = slugify(title)
		if len(slug) == 0:
			raise forms.ValidationError("Please enter a valid tag title.")
		if self.conversation:
			try:
				tag = Tag.objects.get(slug=slug)
			except ObjectDoesNotExist:
				return title
			if tag in self.conversation.tags.all():
				raise forms.ValidationError("That tag is already associated with this conversation.")
		return title
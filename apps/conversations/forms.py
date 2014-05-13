from django import forms
from django.forms import ModelForm
from django.template.defaultfilters import slugify

from models import Conversation, Message

class ConversationForm(ModelForm):

	class Meta:
		model = Conversation
		fields = ['title']

	def clean_title(self):
		title = self.cleaned_data['title']
		slug = slugify(title)
		try:
			convo = Conversation.objects.get(slug=slug)
		except Conversation.DoesNotExist:
			return title
		else:
			if self.instance and convo == self.instance:
				return title
			raise forms.ValidationError("A conversation with that title already exists.")

class ConversationAdminForm(ModelForm):

	class Meta:
		model = Conversation

	def clean_title(self):
		title = self.cleaned_data['title']
		slug = slugify(title)
		try:
			convo = Conversation.objects.get(slug=slug)
		except Conversation.DoesNotExist:
			return title
		else:
			if self.instance and convo == self.instance:
				return title
			raise forms.ValidationError("A conversation with that title already exists.")

class MessageForm(ModelForm):

	class Meta:
		model = Message
		fields = ['text']
		widgets = {
          'text': forms.Textarea(attrs={'rows':5}),
        }

	def clean_text(self):
		text = self.cleaned_data['text']
		slug = slugify(text)
		if len(slug) == 0:
			raise forms.ValidationError("This field is required.")
		return text
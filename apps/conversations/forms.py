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
		if Conversation.objects.filter(slug=slug).exists():
			raise forms.ValidationError("A conversation with that title already exists.")
		return title

class MessageForm(ModelForm):

	class Meta:
		model = Message
		fields = ['text']
		widgets = {
          'text': forms.Textarea(attrs={'rows':6}),
        }
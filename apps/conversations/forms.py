from django import forms
from django.forms import ModelForm

from models import Conversation, Message

class ConversationForm(ModelForm):

	class Meta:
		model = Conversation
		fields = ['title']

class MessageForm(ModelForm):

	class Meta:
		model = Message
		fields = ['text']
		widgets = {
          'text': forms.Textarea(attrs={'rows':6}),
        }
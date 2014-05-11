from django.forms import ModelForm
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from braces.forms import UserKwargModelFormMixin

from models import Tag

class SimpleTagForm(ModelForm):

	class Meta:
		model = Tag
		fields = ('title',)

	def __init__(self, *args, **kwargs):
		super(SimpleTagForm, self).__init__(*args, **kwargs)
		self.fields['title'].label = 'Tag text'
		self.fields['title'].help_text = 'Enter tags separated by a comma.'
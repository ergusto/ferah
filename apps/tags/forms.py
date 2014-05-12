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

	def clean_title(self):
		title = self.cleaned_data['title']
		slug = slugify(title)
		if len(slug) == 0:
			raise forms.ValidationError("Please enter a valid title.")
		try:
			convo = Conversation.objects.get(slug=slug)
		except Conversation.DoesNotExist:
			return title
		else:
			if self.instance and convo == self.instance:
				return title
			raise forms.ValidationError("A conversation with that title already exists.")
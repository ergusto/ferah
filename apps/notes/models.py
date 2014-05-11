from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.

class Note(models.Model):
	user = models.ForeignKey('auth.User', related_name='notes')

	title = models.CharField(max_length=140)
	slug = models.SlugField(max_length=140, editable=False, null=True, blank=True)
	text = models.TextField(max_length=10000)

	date = models.DateTimeField(editable=False, null=True, blank=True)
	modified = models.DateTimeField(editable=False, null=True, blank=True)

	def __unicode__(self):
		return unicode(self.title)

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()
		else:
			self.modified = timezone.now()
		super(Note, self).save(*args, **kwargs)
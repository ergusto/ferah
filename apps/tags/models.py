from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

# Create your models here.

class Tag(models.Model):
	title = models.CharField(max_length=80)
	slug = models.SlugField(editable=False, null=True, blank=True)

	def __unicode__(self):
		return unicode(self.title)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Tag, self).save(*args, **kwargs)

	def first_letter(self):
		return self.title.lower()[0]

	def get_absolute_url(self):
		return reverse('tag_detail', kwargs={
			'slug': self.slug,
		})

	def number_of_conversations(self):
		return self.conversations.all().count()
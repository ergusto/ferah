from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.core.exceptions import ObjectDoesNotExist

from apps.tags.models import Tag

# Create your models here.

class Conversation(models.Model):
	user = models.ForeignKey('auth.User', related_name='owned_conversations')
	participants = models.ManyToManyField('auth.User', related_name='conversations', null=True, blank=True)
	title = models.CharField(max_length=140)
	created = models.DateTimeField(null=True, blank=True, editable=False)
	tags = models.ManyToManyField('tags.Tag', related_name='conversations')
	slug = models.SlugField(editable=False, null=True, blank=True)

	def __unicode__(self):
		return unicode(self.title)

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()
		self.slug = slugify(self.title)
		super(Conversation, self).save(*args, **kwargs)

	def __unicode__(self):
		return unicode(self.title)

	def get_absolute_url(self):
		return reverse('conversation_detail', kwargs={
			'pk': self.id,
		})

	def get_add_message_url(self):
		return reverse('conversation_add_message', kwargs={
			'pk': self.id,
		})

	def get_delete_url(self):
		return reverse('conversation_delete', kwargs={
			'pk': self.id,
		})

	def get_add_tag_url(self):
		return reverse('conversation_add_tag', kwargs={
			'pk': self.id,
		})

	def get_remove_tag_url(self):
		return reverse('conversation_remove_tag', kwargs={
			'pk': self.id,
		})

	def descending_messages(self):
		return self.messages.order_by('-date')

	def add_tag(self, tag_title):
		slug = slugify(tag_title)
		try:
			tag = Tag.objects.get(slug=slug)
		except ObjectDoesNotExist:
			tag = Tag.objects.create(title=tag_title)
		self.tags.add(tag)
		return tag

	def remove_tag(self, tag_text):
		slug = slugify(tag_text)
		try:
			tag = Tag.objects.get(slug=slug)
		except ObjectDoesNotExist:
			pass
		if tag in self.tags.all():
			self.tags.remove(tag)
			self.save()

class Message(models.Model):
	user = models.ForeignKey('auth.User', related_name='sent_messages')
	conversation = models.ForeignKey('conversations.Conversation', related_name='messages')
	
	text = models.CharField(max_length=10000)
	date = models.DateTimeField(null=True, blank=True, editable=False)

	def save(self, *args, **kwargs):
		if not self.id:
			self.date = timezone.now()
		super(Message, self).save(*args, **kwargs)
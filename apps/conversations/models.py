from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.core.exceptions import ObjectDoesNotExist

from apps.tags.models import Tag

# Create your models here.

class Conversation(models.Model):
	BLUE = 'blue'
	PURPLE = 'purple'
	LABEL_CHOICES = (
		(BLUE, 'Fergus'),
		(PURPLE, 'Farah'),
	)

	user = models.ForeignKey('auth.User', related_name='owned_conversations')
	tags = models.ManyToManyField('tags.Tag', related_name='conversations', null=True, blank=True)
	
	title = models.CharField(max_length=140, unique=True)
	slug = models.SlugField(editable=False, unique=True, max_length=140, null=True, blank=True)
	label = models.CharField(max_length=6, choices=LABEL_CHOICES, null=True, blank=True)
	
	created = models.DateTimeField(null=True, blank=True, editable=False)
	last_activity = models.DateTimeField(null=True, blank=True)

	def __unicode__(self):
		return unicode(self.title)

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.localtime(timezone.now())
			self.last_activity = timezone.localtime(timezone.now())
		self.slug = slugify(self.title)
		super(Conversation, self).save(*args, **kwargs)

	def __unicode__(self):
		return unicode(self.title)

	def get_absolute_url(self):
		return reverse('conversation_detail', kwargs={
			'slug': self.slug,
		})

	def get_add_message_url(self):
		return reverse('conversation_add_message', kwargs={
			'slug': self.slug,
		})

	def get_edit_url(self):
		return reverse('conversation_edit', kwargs={
			'slug': self.slug,
		})

	def get_delete_url(self):
		return reverse('conversation_delete', kwargs={
			'slug': self.slug,
		})

	def get_add_tag_url(self):
		return reverse('conversation_add_tag', kwargs={
			'slug': self.slug,
		})

	def get_remove_tag_url(self):
		return reverse('conversation_remove_tag', kwargs={
			'slug': self.slug,
		})

	def descending_messages(self):
		return self.messages.order_by('-date')

	def tag_titles(self):
		tag_titles = []
		for tag in self.tags.all():
			tag_titles.append(tag.title)
			tag_titles.append(' ')
		string = ''.join(tag_titles)
		string = string.strip()
		return string

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

@receiver(pre_save, sender=Conversation)
def slugify_if_title_changed(sender, instance, **kwargs):
	try:
		obj = Conversation.objects.get(pk=instance.pk)
	except Conversation.DoesNotExist:
		pass
	else:
		if not obj.title == instance.title:
			instance.slug = slugify(instance.title)

class Message(models.Model):
	user = models.ForeignKey('auth.User', related_name='sent_messages')
	conversation = models.ForeignKey('conversations.Conversation', related_name='messages')
	
	text = models.TextField(max_length=10000)
	date = models.DateTimeField(null=True, blank=True, editable=False)

	def save(self, *args, **kwargs):
		if not self.id:
			self.date = timezone.localtime(timezone.now())
		self.conversation.last_activity = timezone.localtime(timezone.now())
		self.conversation.save()
		super(Message, self).save(*args, **kwargs)
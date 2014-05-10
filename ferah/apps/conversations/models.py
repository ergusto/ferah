from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.

class Conversation(models.Model):
	user = models.ForeignKey('auth.User', related_name='owned_conversations')
	participants = models.ManyToManyField('auth.User', related_name='conversations')
	title = models.CharField(max_length=140)
	created = models.DateTimeField(null=True, blank=True, editable=False)

	def save(self, *args, **kwargs):
		if not self.id:
			self.created = timezone.now()
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

	def descending_messages(self):
		return self.messages.order_by('-date')

class Message(models.Model):
	user = models.ForeignKey('auth.User', related_name='sent_messages')
	conversation = models.ForeignKey('conversations.Conversation', related_name='messages')
	
	text = models.CharField(max_length=10000)
	date = models.DateTimeField(null=True, blank=True, editable=False)

	def save(self, *args, **kwargs):
		if not self.id:
			self.date = timezone.now()
		super(Message, self).save(*args, **kwargs)
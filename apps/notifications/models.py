from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Notification(models.Model):
	CREATED = 'CR'
	POSTED = 'PO'
	EDITED = 'ED'
	NONE = 'NO'
	ACTION_TYPE_CHOICES = (
		(CREATED, 'created'),
		(EDITED, 'edited'),
		(POSTED, 'posted'),
		(NONE, 'none'),
	)

	user = models.ForeignKey('auth.User', related_name='notifications')
	read = models.BooleanField(default=False)
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey()
	type = models.CharField(max_length=2, choices=ACTION_TYPE_CHOICES, default=EDITED)
	date = models.DateTimeField(null=True, blank=True, editable=False)

	def __unicode__(self):
		return unicode(self.content_object)

	def get_absolute_url(self):
		return reverse('notification_detail', kwargs={
			'pk': self.id,
		})

	def save(self, *args, **kwargs):
		if not self.id:
			self.date = timezone.localtime(timezone.now())
		super(Notification, self).save(*args, **kwargs)
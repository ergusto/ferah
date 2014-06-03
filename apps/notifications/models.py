from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Notification(models.Model):
	CREATED = 'CR'
	EDITED = 'ED'
	NONE = 'NO'
	ACTION_TYPE_CHOICES = (
		(CREATED, 'created'),
		(EDITED, 'edited'),
		(NONE, 'none'),
	)

	user = models.ForeignKey('auth.User', related_name='notifications')
	read = models.BooleanField(default=False)
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey()
	type = models.CharField(max_length=2, choices=ACTION_TYPE_CHOICES, default=EDITED)
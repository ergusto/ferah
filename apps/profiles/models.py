from django.db import models

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField('auth.User', related_name='profile')

	def unread_notifications(self):
		return self.user.notifications.filter(read=False)
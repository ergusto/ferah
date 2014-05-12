from django.contrib import admin

from models import Conversation, Message
from forms import ConversationAdminForm
# Register your models here.

class ConversationAdmin(admin.ModelAdmin):
	form = ConversationAdminForm

admin.site.register(Conversation, ConversationAdmin),
admin.site.register(Message),
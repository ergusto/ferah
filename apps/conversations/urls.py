from django.conf.urls import *
from views import ConversationFormView, ConversationDetailView, ConversationMessageFormView, ConversationDeleteView
from apps.tags.views import AddTagToConversationFormView, RemoveTagFromConversationView

urlpatterns = patterns('',
	url(r'^create/$', ConversationFormView.as_view(), name='conversation_create'),
    url(r'^(?P<pk>\d+)/$', ConversationDetailView.as_view(), name='conversation_detail'),
    url(r'^(?P<pk>\d+)/delete/$', ConversationDeleteView.as_view(), name='conversation_delete'),
    url(r'^(?P<pk>\d+)/message/add/$', ConversationMessageFormView.as_view(), name='conversation_add_message'),
    url(r'^(?P<pk>\d+)/add_tag/$', AddTagToConversationFormView.as_view(), name='conversation_add_tag'),
    url(r'^(?P<pk>\d+)/remove_tag/$', RemoveTagFromConversationView.as_view(), name='conversation_remove_tag'),
)
from django.conf.urls import *
from views import ConversationFormView, ConversationDetailView, ConversationMessageFormView, ConversationDeleteView, ConversationEditView, ConversationExportView, ConversationListView
from apps.tags.views import AddTagToConversationFormView, RemoveTagFromConversationView

urlpatterns = patterns('',
    url(r'^$', ConversationListView.as_view(), name='conversation_list'),
    url(r'^create/$', ConversationFormView.as_view(), name='conversation_create'),
    url(r'^export/$', ConversationExportView.as_view(), name='conversations_export'),
    url(r'^(?P<slug>[-\w]+)/$', ConversationDetailView.as_view(), name='conversation_detail'),
    url(r'^(?P<slug>[-\w]+)/delete/$', ConversationDeleteView.as_view(), name='conversation_delete'),
    url(r'^(?P<slug>[-\w]+)/edit/$', ConversationEditView.as_view(), name='conversation_edit'),
    url(r'^(?P<slug>[-\w]+)/message/add/$', ConversationMessageFormView.as_view(), name='conversation_add_message'),
    url(r'^(?P<slug>[-\w]+)/add_tag/$', AddTagToConversationFormView.as_view(), name='conversation_add_tag'),
    url(r'^(?P<slug>[-\w]+)/remove_tag/$', RemoveTagFromConversationView.as_view(), name='conversation_remove_tag'),
)
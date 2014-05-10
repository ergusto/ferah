from django.conf.urls import *
from views import ConversationFormView, ConversationDetailView, ConversationMessageFormView, ConversationDeleteView

urlpatterns = patterns('',
	url(r'^create/$', ConversationFormView.as_view(), name='conversation_create'),
    url(r'^(?P<pk>\d+)/$', ConversationDetailView.as_view(), name='conversation_detail'),
    url(r'^(?P<pk>\d+)/delete/$', ConversationDeleteView.as_view(), name='conversation_delete'),
    url(r'^(?P<pk>\d+)/message/add/$', ConversationMessageFormView.as_view(), name='conversation_add_message'),
)
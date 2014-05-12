from django.conf.urls import *
from views import TagListView, TagDetailView, TagDeleteView

urlpatterns = patterns('',
    url(r'^$', TagListView.as_view(), name='tags_list'),
    url(r'^(?P<slug>[-\w]+)/$', TagDetailView.as_view(), name='tag_detail'),
    url(r'^(?P<slug>[-\w]+)/delete/$', TagDeleteView.as_view(), name='tag_delete'),
)
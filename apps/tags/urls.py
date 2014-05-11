from django.conf.urls import *
from views import TagListView, TagDetailView

urlpatterns = patterns('',
    url(r'^$', TagListView.as_view(), name='tags_list'),
    url(r'^(?P<slug>[-\w]+)/$', TagDetailView.as_view(), name='tag_detail'),
)
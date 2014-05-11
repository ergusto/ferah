from django.conf.urls import *
from views import TagDetailView

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', TagDetailView.as_view(), name='tag_detail'),
)
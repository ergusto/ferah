from django.conf.urls import *
from views import NotificationListView, NotificationRedirectView

urlpatterns = patterns('',
    url(r'^$', NotificationListView.as_view(), name='notifications'),
    url(r'^(?P<pk>\d+)/$', NotificationRedirectView.as_view(), name='notification_detail'),
)
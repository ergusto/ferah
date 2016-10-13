from django.conf.urls import *
from views import UtilsView

urlpatterns = patterns('',
    url(r'^$', UtilsView.as_view(), name='utils'),
)
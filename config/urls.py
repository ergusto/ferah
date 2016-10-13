from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from rest_framework.routers import DefaultRouter

from apps.conversations.views import RecentMessgaesListView
from apps.conversations.api.views import ConversationViewSet, MessageViewSet
from apps.utils.views import HomeView, UserMessagesView, LoginView

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ferah.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}, name='logout'),
    
    url(r'^me/$', UserMessagesView.as_view(), name='user_detail'),

    url(r'^recent/$', RecentMessgaesListView.as_view(), name='recent_messages'),
    
    (r'^conversations/', include('apps.conversations.urls')),
    (r'^tags/', include('apps.tags.urls')),
    (r'^utils/', include('apps.utils.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
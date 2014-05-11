from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from apps.login.views import LoginView

from apps.home.views import HomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ferah.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}, name='logout'),

    
    (r'^conversations/', include('apps.conversations.urls')),
    (r'^tags/', include('apps.tags.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
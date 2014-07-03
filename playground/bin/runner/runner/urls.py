from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # signup-s urls
    url(r'^$', 'signup.views.home', name='home'),

    url(r'^login/$', 'signup.views.login', name='login'),
    url(r'^profile/$', 'signup.views.profile', name='profile'),
    url(r'^logout/$', 'signup.views.logout', name='logout'),
    url(r'^errorLogin/$', 'signup.views.err_log', name='err_log'),

    #records
    url(r'^record/$', 'record.views.record', name='record'),
    url(r'^records/$', 'record.views.records', name='records'),

    #forum urls
    # url(r'^forum/$', 'forum.views.forum', name='main'),
    # url(r'^forum/(\d+)/$','forum.views.forums', name='forum'),
    # url(r'^thread/(\d+)/$', 'forum.views.thread',name='thread'),

    #highcharts
     #url(r'^bar/$', 'record.views.BarView', name='bar'),

    #admin urls
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)

    urlpatterns+=static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

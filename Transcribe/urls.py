from django.conf.urls.defaults import *
from Transcribe.views import hello, root, register

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^hello/$', hello),
	  ('^transcribe/', include('TranscribeApp.urls', namespace="transcribe")),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/transcribe'}),
    (r'^register/$', register),
   
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)

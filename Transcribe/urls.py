from django.conf.urls.defaults import *
from Transcribe.views import hello, root

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^hello/$', hello),
	('^transcribe/', include('TranscribeApp.urls', namespace="transcribe")),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    
    # Examples:
    # url(r'^$', 'Transcribe.views.home', name='home'),
    # url(r'^Transcribe/', include('Transcribe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

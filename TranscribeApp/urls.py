from django.conf.urls.defaults import *

from TranscribeApp import views


urlpatterns = patterns('', 
	url(r'^$', views.root, name='index'),
	url(r'^test$', views.test, name='index'),
	
	)
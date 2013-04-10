from django.conf.urls import patterns, url

from TranscribeApp import views


urlpatterns = patterns('', 
	url(r'^$', views.root, name='index'),
	url(r'^test$', views.test, name='index'),
	
	)
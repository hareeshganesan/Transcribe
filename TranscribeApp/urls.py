from django.conf.urls.defaults import *

from TranscribeApp import views


urlpatterns = patterns('', 
	url(r'^$', views.root, name='index'),
	url(r'^test$', views.test, name='index2'),
	url(r'^accounts$', views.accounts, name='accounts'),
  url(r'^save$', views.save, name='save'),
	)
from django.conf.urls import url

from . import views

urlspatterns = [
	url(r'^$', views.index, name='index'),
]

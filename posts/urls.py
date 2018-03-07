from django.urls import path, re_path

from . import views

urlpatterns = [
	re_path(r'^posts/create/$', views.create, name='create_post'),
	re_path(r'^posts/(?P<pk>[0-9]+)/$', views.details, name='details')
]
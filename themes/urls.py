from django.urls import path, re_path

from . import views

urlpatterns = [re_path(r'^themes/(?P<pk>[0-9]+)/$', views.details, name='theme_details')
]
"""tests URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
#from . import views
import mainapp.views as mainapp
import posts.views as posts
from django.conf import settings
from django.conf.urls.static import static
"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tutorial/', mainapp.tutorial),
    url(r'^contacts/', mainapp.contacts),
    url(r'^$', mainapp.main),
]
"""
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('tutorial/', mainapp.tutorial, name='tutorial'),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('posts/', posts.index, name='posts'),
    re_path(r'^posts/(?P<pk>[0-9]+)/$', posts.details, name='details'),
    path('', mainapp.main, name = 'name'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
URL configuration for musicapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('faq/', views.faq),
    path('admin/', admin.site.urls),
    path('album/', include('artist.urls')),
    path('artist/', include('artist.urls')),
    path('track/', include('track.urls')),
    path('rendition/', include('rendition.urls')),
    path('upload/', include('upload.urls')),
    path('user/', include('user.urls')),
    path('get/', include('get.urls')),
    path('search/', include('search.urls')),
    path('api/', include('api.urls'))
]

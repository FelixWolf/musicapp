from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/search?type=user', permanent=False)),
    path('login', views.login),
    path('logout', views.logout),
    path('settings', views.userSettings),
    path('me', views.profile),
    path('<uuid:userid>', views.profile)
]

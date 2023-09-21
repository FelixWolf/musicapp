from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/search?type=artist', permanent=False)),
    path('<uuid:artist>', views.artist),
]

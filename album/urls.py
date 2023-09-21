from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from . import view

urlpatterns = [
    path('', RedirectView.as_view(url='/search?type=album', permanent=False)),
    path('<uuid:album>', view.album),
]

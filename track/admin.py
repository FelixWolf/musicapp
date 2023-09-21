from django.contrib import admin
from .models import Track, TrackVote

# Register your models here.
admin.site.register(Track)
admin.site.register(TrackVote)
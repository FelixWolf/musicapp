from django.contrib import admin
from .models import Rendition, RenditionVote

# Register your models here.
admin.site.register(Rendition)
admin.site.register(RenditionVote)
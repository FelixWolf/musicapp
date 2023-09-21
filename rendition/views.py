from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .models import Rendition
import uuid

@never_cache
def rendition(request, rendition):
    try:
        rendition = Rendition.objects.get(id=rendition)
    except Rendition.DoesNotExist:
        return render(request, "rendition404.htm", {}, status = 404)
    
    return render(request, "rendition.htm", {
        "rendition": rendition
    })

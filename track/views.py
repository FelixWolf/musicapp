from django.shortcuts import render
from django.views.decorators.cache import never_cache
from .models import Track
from rendition.models import Rendition
import uuid

@never_cache
def track(request, track):
    try:
        track = Track.objects.get(id=track)
    except Track.DoesNotExist:
        return render(request, "track404.htm", {}, status = 404)
    
    if track.artwork:
        artwork = track.artwork
    elif track.album and track.album.artwork:
        artwork = track.album.artwork
    elif track.artist and track.artist.artwork:
        artwork = track.artist.artwork
    else:
        artwork = uuid.UUID("32dfd1c8-7ff6-5909-d983-6d4adfb4255d")
    
    track.artwork = artwork
    
    return render(request, "track.htm", {
        "track": track
    })

@never_cache
def renditions(request, track):
    try:
        track = Track.objects.get(id=track)
    except Track.DoesNotExist:
        return render(request, "track404.htm", {}, status = 404)
    
    renditions = []
    try:
        renditions = Rendition.objects.filter(track=track)
    except renditions.DoesNotExist:
        pass
    
    return render(request, "renditions.htm", {
        "track": track,
        "renditions": renditions
    })



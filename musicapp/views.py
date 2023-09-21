from django.http import HttpResponse, Http404
from django.views.decorators.cache import never_cache
from django.shortcuts import render

@never_cache
def index(request):
    return render(request, "index.htm", {})

@never_cache
def faq(request):
    return render(request, "faq.htm", {})

@never_cache
def createTestData(request):
    #return HttpResponse("Endpoint locked")
    import json
    import uuid
    from album.models import Album
    from artist.models import Artist
    from track.models import Track
    from rendition.models import Rendition
    with open("/home/felix/Documents/projects/webapps/sample.json", "r") as f:
        data = json.load(f)
    
    print("Deleting renditions")
    Rendition.objects.all().delete()
    print("Deleting tracks")
    Track.objects.all().delete()
    print("Deleting albums")
    Album.objects.all().delete()
    print("Deleting artists")
    Artist.objects.all().delete()
    
    l = len(data["renditions"])
    ri = 0
    renditionLookup = {}
    for rendition in data["renditions"]:
        ri += 1
        print("Inserting rendition {}/{}".format(ri,l), end="\r")
        r = Rendition(id=uuid.UUID(rendition))
        r.duration = data["renditions"][rendition]["duration"]
        r.segmentLength = data["renditions"][rendition]["segmentLength"]
        r.segments = [uuid.UUID(i) for i in data["renditions"][rendition]["segments"]]
        
        r.save()
        renditionLookup[rendition] = r
    print()
    
    artistLookup = {}
    ri = 0
    for track in data["tracks"]:
        ri += 1
        print("Inserting track {}/{}".format(ri,l), end="\r")
        if not (data["tracks"][track]["artist"] in artistLookup):
            try:
                r = Artist.objects.get(name=data["tracks"][track]["artist"])
            except Artist.DoesNotExist:
                r = Artist()
            
            r.name = data["tracks"][track]["artist"]
            r.save()
            artistLookup[data["tracks"][track]["artist"]] = r
        
        t = Track(id = uuid.UUID(track))
        t.artist = artistLookup[data["tracks"][track]["artist"]]
        t.title = data["tracks"][track]["title"]
        t.rendition = renditionLookup[data["tracks"][track]["rendition"]]
        t.save()
        t.rendition.track = t
        t.rendition.save()
    
    print()
    return HttpResponse("Ok!")


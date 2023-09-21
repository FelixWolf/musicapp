from django.shortcuts import render
from django.views.decorators.cache import never_cache

@never_cache
def album(request):
    return render(request, "album.htm", {})
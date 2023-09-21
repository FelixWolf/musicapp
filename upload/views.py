from django.shortcuts import render
from django.views.decorators.cache import never_cache


@never_cache
def upload(request):
    return render(request, "upload.htm", {"success": None})

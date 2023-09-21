from django.shortcuts import render
from django.views.decorators.cache import never_cache


@never_cache
def get(request):
    return render(request, "get.htm")
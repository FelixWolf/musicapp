from django.http import HttpResponse, Http404
from django.views.decorators.cache import never_cache
from django.shortcuts import render

@never_cache
def index(request):
    return render(request, "index.htm", {})

@never_cache
def faq(request):
    return render(request, "faq.htm", {})
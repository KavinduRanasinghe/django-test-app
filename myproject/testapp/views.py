from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the testapp index.")

def test(request):
    return HttpResponse("Hello, world. You're at the testapp test.")

def about(request):
    content =  '<html><body><h1>About</h1><p>This is the about page</p></body></html>'
    return HttpResponse(content)
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, this is the Eclipse Protocol home page. Testing 123.")
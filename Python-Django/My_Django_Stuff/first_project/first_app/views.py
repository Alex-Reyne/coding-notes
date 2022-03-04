from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request): # use 'request' as convention
  return HttpResponse("Hello World!")



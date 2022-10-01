from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def Hello(request):
    return HttpResponse('hello')
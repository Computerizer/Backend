from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'frontend/index.html')

def recents(request):
    return render(request, 'frontend/recents.html')

def post(request, title):
    return render(request, 'frontend/post.html', {
        "title": title
    })    

def about(request):
    return render(request, 'frontend/about.html')
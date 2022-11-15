from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'frontend/index.html')

def post(request, title):
    return render(request, 'frontend/post.html', {
        "title": title
    })    
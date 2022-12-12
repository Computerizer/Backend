from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class List_all_part(APIView):
    """
    Returns a JSON respons of all objects related to a specific part,
    Like all GPUS, CPUS, Cases, Coolers, etc.
    """
    def get(self, request, part):
        pass
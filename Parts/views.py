from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import algorithm
from django.apps import apps
from django.http import JsonResponse
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes

#####################################################################
#####################################################################

@api_view(['POST'])
def algorithm_api(request):
    json = request.data['JSON']
    userPC = algorithm(json)
    generations = 3
    if generations != 0:
        try:
            result = userPC.getComputer()
            return Response(result)
        except Exception:
            print(Exception)
    return Response({'error message': 'maximum user retries, change parameters'})

#####################################################################
#####################################################################
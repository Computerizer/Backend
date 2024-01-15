from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import *
from django.apps import apps
from django.http import JsonResponse, HttpResponseForbidden
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from json import load
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer

#####################################################################
#####################################################################


""" @api_view(['POST'])
def reset_uses(request) -> JsonResponse:
    # Reset the value of 'uses_left' to 3
    request.session['uses_left'] = 3
    # Sends success message
    return JsonResponse({'success': True})

@api_view(['POST'])
def algorithm_api(request):
    if 'uses_left' not in request.session:
        request.session['uses_left'] = 3
    uses = request.session.get('uses_left', None)
    if uses == 0:
        return HttpResponseForbidden('Maximum uses for this session, please reset preferences')
    
    try:
        json = request.data['JSON']
        userPC = algorithm(JSON=json)
        result = userPC.getComputer()
        request.session['uses_left'] -= 1
        return Response(result)
    except Exception:
            print(Exception)
    return Response({'error message': 'maximum user retries, change parameters'})
"""

@api_view(['POST'])
def algorithm_api(request):

    try:
        # Get first part of each category
        data = {
            "CPU": cpu.objects.first().name,
            "GPU": gpu.objects.first().name,
            "RAM": ram.objects.first().name,
            "Motherboard": motherboard.objects.first().name,
            "Storage": ssd.objects.first().name,
            "PSU": psu.objects.first().name,
            "Case": case.objects.first().name,
            "Cooler": aircooler.objects.first().name,
        }
    except:
        return Response({'error message': 'maximum user retries, change parameters'})

    return JsonResponse(data, safe=False)
    #return HttpResponse("Working")

#####################################################################
#####################################################################






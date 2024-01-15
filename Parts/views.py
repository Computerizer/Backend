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
        data = {
            "cpu": cpu.objects.all[0],
            "gpu": gpu.objects.all[0],
            "mobo": motherboard.objects.all[0],
            "cooler": aircooler.objects.all[0],
            "ram": ram.objects.all[0],
            "psu": psu.objects.all[0],
            "storage": [ssd.objects.all[0], hdd.objects.all[0]],
            "case": case.objects.all[0],
        }
    except:
        pass

    return JsonResponse(data, safe=False)
    #return HttpResponse("Working")

#####################################################################
#####################################################################






from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import algorithm, cpuSerializer, moboSerializer, ramSerializer, gpuSerializer, psuSerializer
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
    JSON = {
    'budget': 1500,
    'fps': 144,
    'resolution': '4k',
    'gameType': 'AAA',
    'formFactor': 'ATX',
    'purpose': 'Table Top',
    'theme': 'light',
    'rgb': True
    }

    data = {
        "cpu": {
            "name": "Intel Core i9-9900K 3.6 GHz 8-Core Processor",
            "price": 489.99,
            "rating": 4.9,
            "socket": "LGA1151",
            "cores": 8,
            "clock": 3.6,
            "boost": 5.0,
            "tdp": 95,
            "integrated_graphics": False,
            "smt": True,
            "manufacturer": "Intel"
        },
        "gpu": {
            "name": "NVIDIA GeForce RTX 2080 Ti 11 GB Founders Edition Video Card",
            "price": 1199.99,
            "rating": 4.9,
            "memory": 11,
            "clock": 1350,
            "boost": 1545,
            "tdp": 250,
            "manufacturer": "NVIDIA"
        },
        "mobo": {
            "name": "Asus ROG STRIX Z390-E GAMING ATX LGA1151 Motherboard",
            "price": 239.99,
            "rating": 4.9,
            "socket": "LGA1151",
            "form_factor": "ATX",
            "memory_slots": 4,
            "memory_max": 64,
            "memory_type": "DDR4",
            "manufacturer": "Asus"
        },
        "cooler": {
            "name": "Corsair H100i RGB PLATINUM 75 CFM Liquid CPU Cooler",
            "price": 159.99,
            "rating": 4.9,
            "noise": 37,
            "radiator_size": 240,
            "manufacturer": "Corsair"
        },
        "ram": {
            "name": "Corsair Vengeance RGB Pro 32 GB (2 x 16 GB) DDR4-3200 CL16 Memory",
            "price": 169.99,
            "rating": 4.9,
            "speed": 3200,
            "size": 32,
            "type": "DDR4",
            "manufacturer": "Corsair"
        },
        "psu": {
            "name": "Corsair RM (2019) 750 W 80+ Gold Certified Fully Modular ATX Power Supply",
            "price": 119.99,
            "rating": 4.9,
            "wattage": 750,
            "efficiency": "80+ Gold",
            "modular": True,
            "manufacturer": "Corsair"
        },
        "storage": [
            {
                "name": "Samsung 970 Evo 1 TB M.2-2280 NVME Solid State Drive",
                "price": 179.99,
                "rating": 4.9,
                "size": 1000,
                "type": "M.2-2280 NVME",
                "manufacturer": "Samsung"
            },
            {
                "name": "Seagate Barracuda Compute 2 TB 3.5\" 7200RPM Internal Hard Drive",
                "price": 54.99,
                "rating": 4.9,
                "size": 2000,
                "type": "3.5\" 7200RPM",
                "manufacturer": "Seagate"
            }
        ],
        "case": {
            "name": "Corsair iCUE 4000X RGB ATX Mid Tower Case",
            "price": 119.99,
            "rating": 4.9,
            "form_factor": "ATX Mid Tower",
            "manufacturer": "Corsair"
        }
    }

    return JsonResponse(data, safe=False)

#####################################################################
#####################################################################






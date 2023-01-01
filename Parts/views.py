from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import *
from django.apps import apps
from django.http import JsonResponse
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes
import operator
#####################################################################
#####################################################################
#####################################################################
@api_view(['GET'])
def List_all_cpu(request):
    try:
        name = request.query_params.get('name')
        if name is not None:
            model = cpu.objects.get(name=name)
            serializer = cpuSerializer(model, many=False)
            return Response(serializer.data)
    except ObjectDoesNotExist or MultipleObjectsReturned:
        return Response('CPU not found', status=404)
    try: 
        model = cpu.objects.all()
        serializer = cpuSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
        

        
@api_view(['GET'])
def List_all_gpu(request):
    try:
        name = request.query_params.get('name')
        if name is not None:
            model = gpu.objects.get(name=name)
            serializer = gpuSerializer(model, many=False)
            return Response(serializer.data)
    except ObjectDoesNotExist or MultipleObjectsReturned:
        return Response(f'{name} not found', status=404)
    try: 
        model = gpu.objects.all()
        serializer = gpuSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
        


@api_view(['GET'])
def List_all_ram(request, ):
    try:
        name = request.query_params.get('name')
        if name is not None:
            model = ram.objects.get(name=name)
            serializer = ramSerializer(model, many=False)
            return Response(serializer.data)
    except ObjectDoesNotExist or MultipleObjectsReturned:
        return Response('RAM not found', status=404)
    try: 
        model = ram.objects.all()
        serializer = ramSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_ssd(request, ):
    try:
        name = request.query_params.get('name')
        if name is not None:
            model = ssd.objects.get(name=name)
            serializer = ssdSerializer(model, many=False)
            return Response(serializer.data)
    except ObjectDoesNotExist or MultipleObjectsReturned:
        return Response('SSD not found', status=404)
    try: 
        model = ssd.objects.all()
        serializer = ssdSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_hdd(request, ):
    try:
        name = request.query_params.get('name')
        if name is not None:
            model = hdd.objects.get(name=name)
            serializer = hddSerializer(model, many=False)
            return Response(serializer.data)
    except ObjectDoesNotExist or MultipleObjectsReturned:
        return Response('HDD not found', status=404)
    try: 
        model = hdd.objects.all()
        serializer = hddSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_watercooler(request, ):
    try:
        name = request.query_params.get('name')
        if name is not None:
            model = watercooler.objects.get(name=name)
            serializer = watercoolerSerializer(model, many=False)
            return Response(serializer.data)
    except ObjectDoesNotExist or MultipleObjectsReturned:
        return Response('Watercooler not found', status=404)
    try: 
        model = watercooler.objects.all()
        serializer = watercoolerSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_aircooler(request, ):
    try:
        name = request.query_params.get('name')
        if name is not None:
            model = aircooler.objects.get(name=name)
            serializer = aircoolerSerializer(model, many=False)
            return Response(serializer.data)
    except ObjectDoesNotExist or MultipleObjectsReturned:
        return Response('Aircooler not found', status=404)
    try: 
        model = aircooler.objects.all()
        serializer = aircoolerSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404) 
    


@api_view(['GET'])
def List_all_mobo(request, ):
    try:
        name = request.query_params.get('name')
        if name is not None:
            model = motherboard.objects.get(name=name)
            serializer = moboSerializer(model, many=False)
            return Response(serializer.data)
    except ObjectDoesNotExist or MultipleObjectsReturned:
        return Response('Motherboard not found', status=404)
    try: 
        model = motherboard.objects.all()
        serializer = moboSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_psu(request, ):
    try:
        name = request.query_params.get('name')
        if name is not None:
            model = psu.objects.get(name=name)
            serializer = psuSerializer(model, many=False)
            return Response(serializer.data)
    except ObjectDoesNotExist or MultipleObjectsReturned:
        return Response('PSU not found', status=404)
    try: 
        model = psu.objects.all()
        serializer = psuSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_fan(request, ):
    try:
        name = request.query_params.get('name')
        if name is not None:
            model = fan.objects.get(name=name)
            serializer = fanSerializer(model, many=False)
            return Response(serializer.data)
    except ObjectDoesNotExist or MultipleObjectsReturned:
        return Response('Fan not found', status=404)
    try: 
        model = fan.objects.all()
        serializer = fanSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_case(request, ):
    try:
        name = request.query_params.get('name')
        if name is not None:
            model = case.objects.get(name=name)
            serializer = caseSerializer(model, many=False)
            return Response(serializer.data)
    except ObjectDoesNotExist or MultipleObjectsReturned:
        return Response('Case not found', status=404)
    try: 
        model = case.objects.all()
        serializer = caseSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    
#####################################################################
#####################################################################
#####################################################################



#####################################################################
#####################################################################
#####################################################################
@api_view(['GET'])
def List_specific_cpu(request, manufacturer):
    model = cpu.objects.filter(manufacturer=manufacturer.upper())
    serializer = cpuSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_gpu(request, manufacturer):
    model = gpu.objects.filter(manufacturer=manufacturer.upper())
    serializer = gpuSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_ram(request, manufacturer):
    model = ram.objects.filter(manufacturer=manufacturer.upper())
    serializer = ramSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_ssd(request, manufacturer):
    model = ssd.objects.filter(manufacturer=manufacturer.upper())
    serializer = ssdSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_hdd(request, manufacturer):
    model = hdd.objects.filter(manufacturer=manufacturer.upper())
    serializer = hddSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_watercooler(request, manufacturer):
    model = watercooler.objects.filter(manufacturer=manufacturer.upper())
    serializer = watercoolerSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_aircooler(request, manufacturer):
    model = aircooler.objects.filter(manufacturer=manufacturer.upper())
    serializer = aircoolerSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_mobo(request, manufacturer):
    model = motherboard.objects.filter(manufacturer=manufacturer.upper())
    serializer = moboSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_psu(request, manufacturer):
    model = psu.objects.filter(manufacturer=manufacturer.upper())
    serializer = psuSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_fan(request, manufacturer):
    model = fan.objects.filter(manufacturer=manufacturer.upper())
    serializer = fanSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_case(request, manufacturer):
    model = case.objects.filter(manufacturer=manufacturer.upper())
    serializer = caseSerializer(model, many=True)
    return Response(serializer.data)
#####################################################################
#####################################################################
#####################################################################



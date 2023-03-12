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

#####################################################################
#####################################################################

@api_view(['GET'])
def List_all_cpu(request):
    name = request.query_params.get('name')
    manufacturer = request.query_params.get('manufacturer')
    if name is not None:
        try:
            model = cpu.objects.get(name=name)
            serializer = cpuSerializer(model, many=False)
            return Response(serializer.data)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response('CPU not found', status=404)
    if manufacturer is not None:
        try:
            model = cpu.objects.filter(manufacturer=manufacturer)
            serializer = cpuSerializer(model, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist or Exception:
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
    except:
        pass
    try:
        manufacturer = request.query_params.get('manufacturer')
    except:
        pass
    if name is not None:
        try:
            model = gpu.objects.get(name=name)
            serializer = gpuSerializer(model, many=False)
            return Response(serializer.data)
        except:
            return Response('GPU not found', status=404)
    if manufacturer is not None:
        try:
            model = gpu.objects.filter(manufacturer=manufacturer)
            serializer = gpuSerializer(model, many=True)
            return Response(serializer.data)
        except:
            return Response('GPU not found', status=404)
    try: 
        model = gpu.objects.all()
        serializer = gpuSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
        


@api_view(['GET'])
def List_all_ram(request, ):
    name = request.query_params.get('name')
    manufacturer = request.query_params.get('manufacturer')
    if name is not None:
        try:
            model = ram.objects.get(name=name)
            serializer = ramSerializer(model, many=False)
            return Response(serializer.data)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response('RAM not found', status=404)
    if manufacturer is not None:
        try:
            model = ram.objects.filter(manufacturer=manufacturer)
            serializer = ramSerializer(model, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist or Exception:
            return Response('RAM brand not found', status=404)
    try: 
        model = ram.objects.all()
        serializer = ramSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_ssd(request, ):
    name = request.query_params.get('name')
    manufacturer = request.query_params.get('manufacturer')
    if name is not None:
        try:
            model = ssd.objects.get(name=name)
            serializer = ssdSerializer(model, many=False)
            return Response(serializer.data)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response('SSD not found', status=404)
    if manufacturer is not None:
        try:
            model = ssd.objects.filter(manufacturer=manufacturer)
            serializer = ssdSerializer(model, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist or Exception:
            return Response('SSD brand not found', status=404)
    try: 
        model = ssd.objects.all()
        serializer = ssdSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_hdd(request, ):
    name = request.query_params.get('name')
    manufacturer = request.query_params.get('manufacturer')
    if name is not None:
        try:
            model = hdd.objects.get(name=name)
            serializer = hddSerializer(model, many=False)
            return Response(serializer.data)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response('HDD not found', status=404)
    if manufacturer is not None:
        try:
            model = hdd.objects.filter(manufacturer=manufacturer)
            serializer = hddSerializer(model, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist or Exception:
            return Response('HDD brand not found', status=404)
    try: 
        model = hdd.objects.all()
        serializer = hddSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_watercooler(request, ):
    name = request.query_params.get('name')
    manufacturer = request.query_params.get('manufacturer')
    if name is not None:
        try:
            model = watercooler.objects.get(name=name)
            serializer = watercoolerSerializer(model, many=False)
            return Response(serializer.data)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response('Watercooler not found', status=404)
    if manufacturer is not None:
        try:
            model = watercooler.objects.filter(manufacturer=manufacturer)
            serializer = watercoolerSerializer(model, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist or Exception:
            return Response('Watercooler brand not found', status=404)
    try: 
        model = watercooler.objects.all()
        serializer = watercoolerSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_aircooler(request, ):
    name = request.query_params.get('name')
    manufacturer = request.query_params.get('manufacturer')
    if name is not None:
        try:
            model = aircooler.objects.get(name=name)
            serializer = aircoolerSerializer(model, many=False)
            return Response(serializer.data)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response('Aircooler not found', status=404)
    if manufacturer is not None:
        try:
            model = aircooler.objects.filter(manufacturer=manufacturer)
            serializer = aircoolerSerializer(model, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist or Exception:
            return Response('Aircooler brand not found', status=404)
    try: 
        model = aircooler.objects.all()
        serializer = aircoolerSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_mobo(request, ):
    name = request.query_params.get('name')
    manufacturer = request.query_params.get('manufacturer')
    if name is not None:
        try:
            model = motherboard.objects.get(name=name)
            serializer = moboSerializer(model, many=False)
            return Response(serializer.data)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response('Mobo not found', status=404)
    if manufacturer is not None:
        try:
            model = motherboard.objects.filter(manufacturer=manufacturer)
            serializer = moboSerializer(model, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist or Exception:
            return Response('Mobo brand not found', status=404)
    try: 
        model = motherboard.objects.all()
        serializer = moboSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_psu(request):
    name = request.query_params.get('name')
    manufacturer = request.query_params.get('manufacturer')
    if name is not None:
        try:
            model = psu.objects.get(name=name)
            serializer = psuSerializer(model, many=False)
            return Response(serializer.data)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response('PSU not found', status=404)
    if manufacturer is not None:
        try:
            model = psu.objects.filter(manufacturer=manufacturer)
            serializer = psuSerializer(model, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist or Exception:
            return Response('PSU brand not found', status=404)
    try: 
        model = psu.objects.all()
        serializer = psuSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_fan(request, ):
    name = request.query_params.get('name')
    manufacturer = request.query_params.get('manufacturer')
    if name is not None:
        try:
            model = fan.objects.get(name=name)
            serializer = fanSerializer(model, many=False)
            return Response(serializer.data)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response('Fan not found', status=404)
    if manufacturer is not None:
        try:
            model = fan.objects.filter(manufacturer=manufacturer)
            serializer = fanSerializer(model, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist or Exception:
            return Response('Fan brand not found', status=404)
    try: 
        model = fan.objects.all()
        serializer = fanSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
    


@api_view(['GET'])
def List_all_case(request, ):
    name = request.query_params.get('name')
    manufacturer = request.query_params.get('manufacturer')
    if name is not None:
        try:
            model = case.objects.get(name=name)
            serializer = caseSerializer(model, many=False)
            return Response(serializer.data)
        except ObjectDoesNotExist or MultipleObjectsReturned:
            return Response('Case not found', status=404)
    if manufacturer is not None:
        try:
            model = case.objects.filter(manufacturer=manufacturer)
            serializer = caseSerializer(model, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist or Exception:
            return Response('Case brand not found', status=404)
    try: 
        model = case.objects.all()
        serializer = caseSerializer(model, many=True)
        return Response(serializer.data)
    except Exception:
        return Response(status=404)
#####################################################################
#####################################################################
#####################################################################
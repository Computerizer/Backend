from django.shortcuts import render
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
def List_all_cpu(request, part):
    model = cpu.objects.all()
    serializer = cpuSerializer(model, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def List_all_gpu(request, part):
    model = gpu.objects.all()
    serializer = gpuSerializer(model, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def List_all_ram(request, part):
    model = ram.objects.all()
    serializer = ramSerializer(model, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def List_all_ssd(request, part):
    model = ssd.objects.all()
    serializer = ssdSerializer(model, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def List_all_hdd(request, part):
    model = hdd.objects.all()
    serializer = hddSerializer(model, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def List_all_watercooler(request, part):
    model = watercooler.objects.all()
    serializer = watercoolerSerializer(model, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def List_all_aircooler(request, part):
    model = aircooler.objects.all()
    serializer = aircoolerSerializer(model, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def List_all_mobo(request, part):
    model = motherboard.objects.all()
    serializer = moboSerializer(model, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def List_all_psu(request, part):
    model = psu.objects.all()
    serializer = psuSerializer(model, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def List_all_fan(request, part):
    model = fan.objects.all()
    serializer = fanSerializer(model, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def List_all_case(request, part):
    model = case.objects.all()
    serializer = case(model, many=True)
    return Response(serializer.data)
    
#####################################################################
#####################################################################
#####################################################################



#####################################################################
#####################################################################
#####################################################################
@api_view(['GET'])
def List_specific_cpu(request, part, manufacturer):
    model = cpu.objects.filter(manufacturer=manufacturer.upper())
    serializer = cpuSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_gpu(request, part, manufacturer):
    model = gpu.objects.filter(manufacturer=manufacturer.upper())
    serializer = gpuSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_ram(request, part, manufacturer):
    model = ram.objects.filter(manufacturer=manufacturer.upper())
    serializer = ramSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_ssd(request, part, manufacturer):
    model = ssd.objects.filter(manufacturer=manufacturer.upper())
    serializer = ssdSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_hdd(request, part, manufacturer):
    model = hdd.objects.filter(manufacturer=manufacturer.upper())
    serializer = hddSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_watercooler(request, part, manufacturer):
    model = watercooler.objects.filter(manufacturer=manufacturer.upper())
    serializer = watercoolerSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_aircooler(request, part, manufacturer):
    model = aircooler.objects.filter(manufacturer=manufacturer.upper())
    serializer = aircoolerSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_mobo(request, part, manufacturer):
    model = motherboard.objects.filter(manufacturer=manufacturer.upper())
    serializer = moboSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_psu(request, part, manufacturer):
    model = psu.objects.filter(manufacturer=manufacturer.upper())
    serializer = psuSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_fan(request, part, manufacturer):
    model = fan.objects.filter(manufacturer=manufacturer.upper())
    serializer = fanSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_case(request, part, manufacturer):
    model = case.objects.filter(manufacturer=manufacturer.upper())
    serializer = caseSerializer(model, many=True)
    return Response(serializer.data)
#####################################################################
#####################################################################
#####################################################################



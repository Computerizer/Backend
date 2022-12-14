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

@api_view(['GET'])
def List_all_part(request, part):
    table = apps.get_model('Parts', part)
    model = table.objects.all()
    if part.lower() == 'cpu':
        serializer = cpuSerializer(model, many=True)
    if part.lower() == 'gpu':
        serializer = gpuSerializer(model, many=True)
    if part.lower() == 'ram':
        serializer = ramSerializer(model, many=True)
    if part.lower() == 'ssd':
        serializer = ssdSerializer(model, many=True)
    if part.lower() == 'hdd':
        serializer = hddSerializer(model, many=True)
    if part.lower() == 'watercooler':
        serializer = watercoolerSerializer(model, many=True)
    if part.lower() == 'aircooler':
        serializer = aircoolerSerializer(model, many=True)
    if part.lower() == 'mobo' or part.lower() == 'motherboard':
        serializer = moboSerializer(model, many=True)
    if part.lower() == 'psu':
        serializer = psuSerializer(model, many=True)
    if part.lower() == 'fan':
        serializer = fanSerializer(model, many=True)
    if part.lower() == 'case':
        serializer = caseSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_part(request, part, manufacturer):
    table = apps.get_model('Parts', part)
    model = table.objects.filter(manufacturer=manufacturer.upper())
    if part.lower() == 'cpu':
        serializer = cpuSerializer(model, many=True)
    if part.lower() == 'gpu':
        serializer = gpuSerializer(model, many=True)
    if part.lower() == 'ram':
        serializer = ramSerializer(model, many=True)
    if part.lower() == 'ssd':
        serializer = ssdSerializer(model, many=True)
    if part.lower() == 'hdd':
        serializer = hddSerializer(model, many=True)
    if part.lower() == 'watercooler':
        serializer = watercoolerSerializer(model, many=True)
    if part.lower() == 'aircooler':
        serializer = aircoolerSerializer(model, many=True)
    if part.lower() == 'mobo' or part.lower() == 'motherboard':
        serializer = moboSerializer(model, many=True)
    if part.lower() == 'psu':
        serializer = psuSerializer(model, many=True)
    if part.lower() == 'fan':
        serializer = fanSerializer(model, many=True)
    if part.lower() == 'case':
        serializer = caseSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def List_specific_part(request, part, manufacturer):
    table = apps.get_model('Parts', part)
    model = table.objects.filter(manufacturer=manufacturer.upper())
    if part.lower() == 'cpu':
        serializer = cpuSerializer(model, many=True)
    if part.lower() == 'gpu':
        serializer = gpuSerializer(model, many=True)
    if part.lower() == 'ram':
        serializer = ramSerializer(model, many=True)
    if part.lower() == 'ssd':
        serializer = ssdSerializer(model, many=True)
    if part.lower() == 'hdd':
        serializer = hddSerializer(model, many=True)
    if part.lower() == 'watercooler':
        serializer = watercoolerSerializer(model, many=True)
    if part.lower() == 'aircooler':
        serializer = aircoolerSerializer(model, many=True)
    if part.lower() == 'mobo' or part.lower() == 'motherboard':
        serializer = moboSerializer(model, many=True)
    if part.lower() == 'psu':
        serializer = psuSerializer(model, many=True)
    if part.lower() == 'fan':
        serializer = fanSerializer(model, many=True)
    if part.lower() == 'case':
        serializer = caseSerializer(model, many=True)
    return Response(serializer.data)



from django.shortcuts import render
from .models import cpu
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes


@api_view(['GET'])
def List_all_part(request, part):
    if part.lower() == 'cpu': 
        model = cpu.objects.all()
        serializer = CpuSerializer(model, many=True)

    if part.lower() == 'gpu': 
        model = gpu.objects.all()
        serializer = GpuSerializer(model, many=True)

    if part.lower() == 'ram': 
        model = ram.objects.all()
        serializer = RamSerializer(model, many=True)

    if part.lower() == 'motherboard': 
        model = motherboard.objects.all()
        serializer = MoboSerializer(model, many=True)

    if part.lower() == 'ssd': 
        model = ssd.objects.all()
        serializer = SsdSerializer(model, many=True)

    if part.lower() == 'hdd': 
        model = hdd.objects.all()
        serializer = HddSerializer(model, many=True)

    if part.lower() == 'case': 
        model = case.objects.all()
        serializer = CaseSerializer(model, many=True)

    if part.lower() == 'fan': 
        model = fan.objects.all()
        serializer = FanSerializer(model, many=True)

    if part.lower() == 'aircooler': 
        model = aircooler.objects.all()
        serializer = AircoolerSerializer(model, many=True)
    
    if part.lower() == 'watercooler': 
        model = watercooler.objects.all()
        serializer = WatercoolerSerializer(model, many=True)
    
    return Response(serializer.data)


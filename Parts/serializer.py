from rest_framework.serializers import ModelSerializer
from .models import *

class CPUSerializer(ModelSerializer):
    class Meta:
        model = cpu
        fields = '__all__'

class GPUSerializer(ModelSerializer):
    class Meta:
        model = gpu
        fields = '__all__'

class RAMSerializer(ModelSerializer):
    class Meta:
        model = ram
        fields = '__all__'

class AirCoolerSerializer(ModelSerializer):
    class Meta:
        model = aircooler
        fields = '__all__'

class WaterCoolerSerializer(ModelSerializer):
    class Meta:
        model = watercooler
        fields = '__all__'

class PsuSerializer(ModelSerializer):
    class Meta:
        model = psu
        fields = '__all__'

class MotherboardSerializer(ModelSerializer):
    class Meta:
        model = motherboard
        fields = '__all__'

class HddSerializer(ModelSerializer):
    class Meta:
        model = hdd
        fields = '__all__'

class SsdSerializer(ModelSerializer):
    class Meta:
        model = ssd
        fields = '__all__'

class CaseSerializer(ModelSerializer):
    class Meta:
        model = case
        fields = '__all__'

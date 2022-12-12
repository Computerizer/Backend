from rest_framework.serializers import ModelSerializer, Serializer
from .models import *

class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = manufacturer
        fields = '__all__'

############################################
#       Serializers for specific parts     # 
############################################
class CpuSerializer(ModelSerializer):
    class Meta:
        model = cpu
        fields = '__all__'

class GpuSerializer(ModelSerializer):
    class Meta:
        model = gpu
        fields = '__all__'

class RamSerializer(ModelSerializer):
    class Meta:
        model = ram
        fields = '__all__'

class SsdSerializer(ModelSerializer):
    class Meta:
        model = ssd
        fields = '__all__'

class HddSerializer(ModelSerializer):
    class Meta:
        model = hdd
        fields = '__all__'

class WatercoolerSerializer(ModelSerializer):
    class Meta:
        model = watercooler
        fields = '__all__'

class AircoolerSerializer(ModelSerializer):
    class Meta:
        model = aircooler
        fields = '__all__'

class PsuSerializer(ModelSerializer):
    class Meta:
        model = psu
        fields = '__all__'

class FanSerializer(ModelSerializer):
    class Meta:
        model = fan
        fields = '__all__'

class CaseSerializer(ModelSerializer):
    class Meta:
        model = case
        fields = '__all__'
############################################
############################################

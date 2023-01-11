from rest_framework.serializers import ModelSerializer, Serializer
from .models import *

class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = manufacturer
        fields = '__all__'

############################################
#       Serializers for specific parts     # 
############################################
class cpuSerializer(ModelSerializer):
    class Meta:
        model = cpu
        fields = '__all__'

class gpuSerializer(ModelSerializer):
    class Meta:
        model = gpu
        fields = '__all__'

class ramSerializer(ModelSerializer):
    class Meta:
        model = ram
        fields = '__all__'

class ssdSerializer(ModelSerializer):
    class Meta:
        model = ssd
        fields = '__all__'

class hddSerializer(ModelSerializer):
    class Meta:
        model = hdd
        fields = '__all__'

class watercoolerSerializer(ModelSerializer):
    class Meta:
        model = watercooler
        fields = '__all__'

class aircoolerSerializer(ModelSerializer):
    class Meta:
        model = aircooler
        fields = '__all__'

class moboSerializer(ModelSerializer):
    class Meta:
        model = motherboard
        fields = '__all__'

class psuSerializer(ModelSerializer):
    class Meta:
        model = psu
        fields = '__all__'

class fanSerializer(ModelSerializer):
    class Meta:
        model = fan
        fields = '__all__'

class caseSerializer(ModelSerializer):
    class Meta:
        model = case
        fields = '__all__'
############################################
############################################

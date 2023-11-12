'''from rest_framework.serializers import ModelSerializer, Serializer

############################################
#       Serializers for specific parts     # 
############################################
class cpuSerializer(ModelSerializer):
    class Meta:
        from .models import cpu
        model = cpu
        fields = '__all__'

class gpuSerializer(ModelSerializer):
    class Meta:
        from .models import gpu
        model = gpu
        fields = '__all__'

class ramSerializer(ModelSerializer):
    class Meta:
        from .models import ram
        model = ram
        fields = '__all__'

class ssdSerializer(ModelSerializer):
    class Meta:
        from .models import ssd
        model = ssd
        fields = '__all__'

class hddSerializer(ModelSerializer):
    class Meta:
        from .models import hdd
        model = hdd
        fields = '__all__'

class watercoolerSerializer(ModelSerializer):
    class Meta:
        from .models import watercooler
        model = watercooler
        fields = '__all__'

class aircoolerSerializer(ModelSerializer):
    class Meta:
        from .models import aircooler
        model = aircooler
        fields = '__all__'

class moboSerializer(ModelSerializer):
    class Meta:
        from .models import motherboard
        model = motherboard
        fields = '__all__'

class psuSerializer(ModelSerializer):
    class Meta:
        from .models import psu
        model = psu
        fields = '__all__'

class fanSerializer(ModelSerializer):
    class Meta:
        from .models import fan
        model = fan
        fields = '__all__'

class caseSerializer(ModelSerializer):
    class Meta:
        from .models import case
        model = case
        fields = '__all__'
'''
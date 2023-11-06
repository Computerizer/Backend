from rest_framework import serializers

from .models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('username','email','password','sub_to_newsletter','own_pc')
class FindUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('__all__')
class AllUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('__all__')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=('email','password')
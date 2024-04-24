from rest_framework import serializers

from .models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('username','email','password','sub_to_newsletter','own_pc')

        def create(self, validated_data):
            user = CustomUser(
                email=validated_data['email'],
                username=validated_data['username'],
                profile_pic = validated_data['profile_pic'],
                sub_to_newsletter = validated_data['sub_to_newsletter'],
                own_pc = validated_data["own_pc"]
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
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
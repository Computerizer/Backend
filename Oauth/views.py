from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializer import *
from django.contrib.auth import login, authenticate,logout
from rest_framework.authentication import TokenAuthentication
import json
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView

class Register(APIView):
    authentication_classes = ([])
    permission_classes = ([AllowAny])
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.set_password(request.data['password'])
            account.save()
            token = Token.objects.create(user=account)
            return Response({
                "response":"User Created Successfully",
                'username': account.username,
                'email': account.email,
                'sub_to_newsletter': account.sub_to_newsletter,
                'own_pc': account.own_pc,
                "token": token.key,
                },status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    authentication_classes = ([])
    permission_classes = ([AllowAny])
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        try:
            Account = CustomUser.objects.get(email=email)
        except BaseException as e:
            return Response({"response": "Incorrect Login credentials"})

        if not check_password(password, Account.password):
            return Response({"response": "Incorrect Login credentials"})
        
        token, create = Token.objects.get_or_create(user=Account)
        print(token)
        if Account:
            if Account.is_active:
                data = {}
                login(request, user=Account)
                data["response"] = "user logged in"
                data["email"] = email
                data['username'] =  Account.username
                data['toke'] = token.key
                return Response(data)
            else:
                raise ValidationError({"400": f'Account not active'})
        else:
            raise ValidationError({"400": f'Account doesnt exist'})

class Logout(APIView):
    authentication_classes = ([])
    permission_classes = ([AllowAny])
    def post(self,request):
        try:
            Token.objects.filter(key=request.data['token']).delete()
        except (AttributeError):
            return Response({"Error": "Error"},status=status.HTTP_400_BAD_REQUEST)

        logout(request)

        return Response({"success": ("Successfully logged out.")},status=status.HTTP_200_OK)
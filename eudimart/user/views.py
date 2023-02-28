from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

from .models import Userdata , Tweet
from .serializers import UserdataSerializers
from .serializers import TweetSerializer
from rest_framework import generics


class Userviewset(viewsets.ModelViewSet):
    queryset = Userdata.objects.all()
    serializer_class = UserdataSerializers


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class TweetDelete(APIView):
   def delete(self, request, id=None):
        tweet = Tweet.objects.filter(id=id)
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




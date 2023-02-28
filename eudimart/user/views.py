from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Userdata, Tweet
from .serializers import UserdataSerializers
from .serializers import TweetSerializer



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




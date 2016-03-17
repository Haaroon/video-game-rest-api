from videogames.models import *
from videogames.serializers import *
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

class VideoGameList(generics.ListCreateAPIView):
    queryset = VideoGame.objects.all()
    serializer_class = VideoGameSerializer

class VideoGameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoGame.objects.all()
    serializer_class = VideoGameSerializer
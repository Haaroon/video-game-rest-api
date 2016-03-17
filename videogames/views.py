from videogames.models import *
from videogames.serializers import *
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from videogames.permissions import IsOwnerOrReadOnly


class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class VideoGameList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = VideoGame.objects.all()
    serializer_class = VideoGameSerializer
   
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class VideoGameDetail(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
    queryset = VideoGame.objects.all()
    serializer_class = VideoGameSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
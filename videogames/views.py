from videogames.models import *
from videogames.serializers import *
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins
from django.contrib.auth.models import User
from rest_framework import permissions
from videogames.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
import json

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

class VideoGameViewSet(viewsets.ModelViewSet):
    queryset = VideoGame.objects.all()
    serializer_class = VideoGameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
 
    def get_queryset(self):
        print("In get query set, query params is : ", self.request.query_params)
        queryset = VideoGame.objects.all()
        searchGenre = self.request.query_params.get('genre', None)
        searchDeveloper = self.request.query_params.get('developer', None)
        searchPlatform = self.request.query_params.get('platform', None)
        searchRating = self.request.query_params.get('rating', None)
        searchOwner = self.request.query_params.get('owner', None)

        if searchGenre is not None:
            queryset = queryset.filter(genre=searchGenre)
        if searchDeveloper is not None:
            queryset = queryset.filter(developer=searchDeveloper)
        if searchPlatform is not None:
            queryset = queryset.filter(platform=searchPlatform)
        if searchRating is not None:
            queryset = queryset.filter(rating=searchRating)
        if searchOwner is not None:
                queryset = queryset.filter(owner=searchOwner)
            
        return queryset

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
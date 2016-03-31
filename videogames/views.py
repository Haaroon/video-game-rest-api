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

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PlatformViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class DeveloperViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

    def get_queryset(self):
        print("In get query set, query params is : ", self.request.query_params)
        queryset = Review.objects.all()
        searchHeading = self.request.query_params.get('heading', None)
        searchBody = self.request.query_params.get('body', None)
        searchRating = self.request.query_params.get('rating', None)
        searchGame = self.request.query_params.get('game', None)
        searchUsername = self.request.query_params.get('username', None)

        if searchHeading is not None:
            queryset = queryset.filter(heading__icontains=searchHeading)
        if searchBody is not None:
            queryset = queryset.filter(body__icontains=searchBody)
        if searchGame is not None:
            queryset = queryset.filter(game__title__icontains=searchGame)
        if searchRating is not None:
            queryset = queryset.filter(rating=searchRating)
        if searchUsername is not None:
                queryset = queryset.filter(username__username__icontains=searchUsername)
            
        return queryset

class VideoGameViewSet(viewsets.ModelViewSet):
    queryset = VideoGame.objects.all()
    serializer_class = VideoGameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
 
    def get_queryset(self):
        print("In get query set, query params is : ", self.request.query_params)
        queryset = VideoGame.objects.all()
        searchTitle = self.request.query_params.get('title', None)
        searchGenre = self.request.query_params.get('genre', None)
        searchDeveloper = self.request.query_params.get('developer', None)
        searchPlatform = self.request.query_params.get('platform', None)
        searchRating = self.request.query_params.get('rating', None)
        searchOwner = self.request.query_params.get('owner', None)

        if searchTitle is not None:
            queryset = queryset.filter(title__icontains=searchTitle)
        if searchGenre is not None:
            queryset = queryset.filter(genre=searchGenre)
        if searchDeveloper is not None:
            queryset = queryset.filter(developer__developer__icontains=searchDeveloper)
        if searchPlatform is not None:
            queryset = queryset.filter(platform__platform__icontains=searchPlatform)
        if searchRating is not None:
            queryset = queryset.filter(rating=searchRating)
        if searchOwner is not None:
            queryset = queryset.filter(owner=searchOwner)
            
        return queryset

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
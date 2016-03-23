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

class GameGenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VideoGame.objects.all()
    serializer_class = VideoGameSerializer

class PlatformViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class PublisherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class DeveloperViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

class RatingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class MaxPlayersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MaxPlayers.objects.all()
    serializer_class = MaxPlayersSerializer

class AgeRatingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AgeRating.objects.all()
    serializer_class = AgeRatingSerializer

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
        searchPublisher = self.request.query_params.get('publisher', None)
        searchPlatform = self.request.query_params.get('platform', None)
        searchRating = self.request.query_params.get('rating', None)
        searchMaxPlayers = self.request.query_params.get('maxPlayers', None)
        searchHasMultiplayer = self.request.query_params.get('hasMultiplayer', None)
        searchAgeRating = self.request.query_params.get('ageRating', None)
        searchOwner = self.request.query_params.get('owner', None)

        if searchGenre is not None:
            queryset = queryset.filter(genre=searchGenre)
        if searchDeveloper is not None:
            queryset = queryset.filter(developer=searchDeveloper)
        if searchPublisher is not None:
            queryset = queryset.filter(publisher=searchPublisher)
        if searchPlatform is not None:
            queryset = queryset.filter(platform=searchPlatform)
        if searchRating is not None:
            queryset = queryset.filter(rating=searchRating)
        if searchMaxPlayers is not None:
            queryset = queryset.filter(maxPlayers=searchMaxPlayers)
        if searchHasMultiplayer is not None:
            queryset = queryset.filter(hasMultiplayer=searchHasMultiplayer)
        if searchAgeRating is not None:
            queryset = queryset.filter(ageRating=searchAgeRating)
        if searchOwner is not None:
                queryset = queryset.filter(owner=searchOwner)
            
        return queryset

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
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
        
class VideoGameViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = VideoGame.objects.all()
    serializer_class = VideoGameSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            genre = Genre.objects.get_or_create(genre=serializer.validated_data['genre'])
            platform = Platform.objects.get_or_create(platform=serializer.validated_data['platform'])
            developer = Developer.objects.get_or_create(developer=serializer.validated_data['developer'])
            publisher = Publisher.objects.get_or_create(publisher=serializer.validated_data['publisher'])
            rating = Rating.objects.get_or_create(rating=serializer.validated_data['rating'])
            maxPlayers = MaxPlayers.objects.get_or_create(maxPlayers=serializer.validated_data['maxPlayers'])
            ageRating = AgeRating.objects.get_or_create(ageRating=serializer.validated_data['ageRating'])
            VideoGame.objects.create(
                title  = serializer.validated_data["title"],
                description = serializer.validated_data["description"],
                brief = serializer.validated_data["brief"],
                genre = genre[0],
                platform = platform[0],
                developer = developer[0], 
                publisher = publisher[0],
                rating = rating[0],
                maxPlayers=maxPlayers[0],
                hasMultiplayer=serializer.validated_data["hasMultiplayer"],
                ageRating=ageRating[0],
                owner=self.request.user)
            results = VideoGame.objects.get(title=serializer.validated_data["title"]).on_success()
            # return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            return Response(results, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'Video Game could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

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
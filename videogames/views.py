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

class PublisherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class DeveloperViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer

class RatingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

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
            genre = Genre.objects.get_or_create(genre=serializer.validated_data['genres'])
            platform = Platform.objects.get_or_create(platform=serializer.validated_data['platforms'])
            developer = Developer.objects.get_or_create(developer=serializer.validated_data['developers'])
            publisher = Publisher.objects.get_or_create(publisher=serializer.validated_data['publishers'])
            rating = Rating.objects.get_or_create(rating=serializer.validated_data['rating'])
            VideoGame.objects.create(
                title  = serializer.validated_data["title"],
                description = serializer.validated_data["description"],
                brief = serializer.validated_data["brief"],
                genres = genre[0],
                platforms = platform[0],
                developers = developer[0], 
                publishers = publisher[0],
                rating = rating[0],
                owner=self.request.user)
            results = VideoGame.objects.get(title=serializer.validated_data["title"]).as_json()
            # return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            return Response(results, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'Video Game could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
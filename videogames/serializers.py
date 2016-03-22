from rest_framework import serializers
from videogames.models import *
from django.contrib.auth.models import User
from django.utils.encoding import force_text


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class MaxPlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaxPlayers
        fields = '__all__'

class AgeRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeRating
        fields = '__all__'

class VideoGameSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    genre = serializers.SlugRelatedField(
        # many=True,
        # read_only=True,
        slug_field='genre',
        queryset=Genre.objects.all()
     )
    platform =  serializers.SlugRelatedField(
        # many=True,
        # read_only=True,
        slug_field='platform',
        queryset=Platform.objects.all()
     )
    publisher = serializers.SlugRelatedField(
        # many=True,
        # read_only=True,
        slug_field='publisher',
        queryset=Publisher.objects.all()
     )
    developer = serializers.SlugRelatedField(
        # many=True,
        # read_only=True,
        slug_field='developer',
        queryset=Developer.objects.all()
     )
    rating = serializers.SlugRelatedField(
        # many=True,
        # read_only=True,
        slug_field='rating',
        queryset=Rating.objects.all()
     )
    ageRating = serializers.SlugRelatedField(
        # many=True,
        # read_only=True,
        slug_field='ageRating',
        queryset=AgeRating.objects.all()
     )
    maxPlayers = serializers.SlugRelatedField(
        # many=True,
        # read_only=True,
        slug_field='maxPlayers',
        queryset=MaxPlayers.objects.all()
     )

    class Meta:
        model = VideoGame
        fields = ('title', 'description', 'brief', 'genre',
                   'platform', 'publisher', 'developer', 'rating', 
                   'ageRating', 'maxPlayers', 'hasMultiplayer', 'owner', )
        depth = 2


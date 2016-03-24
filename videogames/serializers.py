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

class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = [ 'platform', 'manufactorer', 'consoleType', 'url']

class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = [ 'publisher', 'headquarters', 'market', 'url']

class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Developer
        fields = [ 'developer', 'headquarters', 'market', 'url']

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

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['username']

class VideoGameSerializer(serializers.ModelSerializer):
    platform = PlatformSerializer()
    publisher = PublisherSerializer()
    developer =  DeveloperSerializer()
    class Meta:
        model = VideoGame
        fields = [ "title", "description", "brief", "hasMultiplayer",
                    "genre", "platform", "publisher", "developer", "rating",
                    "maxPlayers", "ageRating" ]
        # exclude = ['owner']

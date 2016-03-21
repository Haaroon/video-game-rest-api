from rest_framework import serializers
from videogames.models import *
from django.contrib.auth.models import User
from django.utils.encoding import force_text


class UserSerializer(serializers.ModelSerializer):
    # videogames = serializers.PrimaryKeyRelatedField(many=True, queryset=VideoGame.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username') #,'videogames')

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

class VideoGameSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    genres = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    platforms = serializers.PrimaryKeyRelatedField(queryset=Platform.objects.all())
    publishers = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all())
    developers = serializers.PrimaryKeyRelatedField(queryset=Developer.objects.all())
    rating = serializers.PrimaryKeyRelatedField(queryset=Rating.objects.all())

    class Meta:
        model = VideoGame
        fields = ('title', 'description', 'brief', 'genres', 'platforms', 'publishers',
                     'developers', 'rating', 'release_date', 'owner', )
        depth = 2


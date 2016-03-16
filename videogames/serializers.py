from rest_framework import serializers
from videogames.models import *


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

class VideoGameSerializer(serializers.ModelSerializer):
    # genres = GenreSerializer()
    # platforms = PlatformSerializer()
    # publishers = PublisherSerializer()
    # developers = DeveloperSerializer()
    # rating = RatingSerializer()
    class Meta:
        model = VideoGame
        fields = ('title', 'description', 'brief', 'genres', 'platforms', 'publishers', 'developers', 'rating', 'release_date')
        depth = 2

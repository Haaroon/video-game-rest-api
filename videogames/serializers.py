from rest_framework import serializers
from videogames.models import *
from django.contrib.auth.models import User
from django.utils.encoding import force_text

# Serializer to only show user data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

# Serailzier for to show all data when linked is pressed
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

# Serailzier for to show all data when linked is pressed
class GenreSingleSerializer(serializers.ModelSerializer):
    # links = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = '__all__'

    # def get_links(self, obj):
    #     request = self.context['request']
    #     return {
    #         'All Genres': reverse('genre-list', request=request),
    #     } 

# Serailzier for to show all data when linked is pressed
class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

# Serailzier for to show all data when linked is pressed
class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class VideoGameLimitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideoGame
        fields = ['url', 'title']

# Serializer that displayus infrmation about reviews
class ReviewSerializer(serializers.ModelSerializer):
   
    username = UserSerializer(read_only=True)
    # links = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = [ "heading", "body", "rating", "videogame", "username", ]
        # fields = [ "heading", "body", "rating", "videogame", "username", "links"]

    # def get_links(self, obj):
    #     request = self.context['request']
    #     return {
    #         'All Reviews': reverse('review-list', request=request),
    #     } 

# Serializer that shows all video games
class VideoGameSerializer(serializers.ModelSerializer):
    genre = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        view_name='genre-detail'
    )

    platform = serializers.HyperlinkedRelatedField(
        many=False,
        queryset=Platform.objects.all(),
        view_name='platform-detail'
    )

    videogame_review = serializers.HyperlinkedRelatedField(
        many=True, 
        view_name="review-detail", 
        read_only=True
    )

    class Meta:
        model = VideoGame
        fields = [ "url", "title", "description", "brief",
                   "genre", "platform", "developer", "videogame_review", ]

class VideoGameLimitSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.PrimaryKeyRelatedField(queryset=VideoGame.objects.all())

    class Meta:
        model = VideoGame
        fields = [ "title", "url" ]
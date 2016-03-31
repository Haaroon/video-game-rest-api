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
    videogame = VideoGameLimitSerializer()
    username = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [ "heading", "body", "rating", "videogame", "username"]

    # def create(self, validated_data):
    #     print(self)
    #     new_review = Review.objects.create(
    #             heading=validated_data.get("heading"),
    #             body=validated_data.get("body"),
    #             rating=validated_data.get("rating"),
    #             username=validated_data.get("username"),
    #             # game=validated_data.get("game")['title'],
    #     )
    #     return new_review

# Serializer that shows all video games
class VideoGameSerializer(serializers.ModelSerializer):
    genre = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        view_name='genre-detail'
    )

    platform = PlatformSerializer()

    videogame_review = serializers.HyperlinkedRelatedField(
        many=True, 
        view_name="review-detail", 
        read_only=True
    )

    class Meta:
        model = VideoGame
        fields = [ "url", "title", "description", "brief",
                   "genre", "platform", "developer", "videogame_review"  ]

class VideoGameLimitSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.PrimaryKeyRelatedField(queryset=VideoGame.objects.all())

    class Meta:
        model = VideoGame
        fields = [ "title", "url" ]

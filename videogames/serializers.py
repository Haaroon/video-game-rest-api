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
class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

# Serailzier for to show all data when linked is pressed
class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

# Serializer that displayus infrmation about reviews
class ReviewSerializer(serializers.ModelSerializer):
    # game = VideoGameLimitSerializer()
    username = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [ "heading", "body", "rating", "videogame", "username"]
        # extra_kwargs = {'url': {'view_name': 'review-detail'}} 
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
    platform =  serializers.HyperlinkedRelatedField(
        many=True,
        queryset=Platform.objects.all(),
        view_name='platform-detail'
    )

    genre = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        view_name='genre-detail'
    )

    developer =  serializers.HyperlinkedRelatedField(
        many=False,
        queryset=Developer.objects.all(),
        view_name='developer-detail'
    )

    videogame_review = serializers.HyperlinkedRelatedField(
        many=True, 
        view_name="review-detail", 
        read_only=True
    )
    
    class Meta:
        model = VideoGame
        # fields = "__all__"
        fields = [ "url", "title", "description", "brief",
                   "genre", "platform", "developer", "videogame_review" ]

    # def create(self, validated_data):
    #     print(validated_data.get("owner"))
    #     game_data = VideoGame.objects.create(
    #             title=validated_data.get("title"),
    #             description=validated_data.get("description"),
    #             brief=validated_data.get("brief"),
    #             # genre=validated_data.get("genre")['genre'],
    #             platform=validated_data.get("platform")['platform'],
    #             developer=validated_data.get("developer")['developer'],
    #             owner=validated_data.get("owner"),
    #     )
    #     return game_data

class VideoGameLimitSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.PrimaryKeyRelatedField(queryset=VideoGame.objects.all())

    class Meta:
        model = VideoGame
        fields = [ "title", "url" ]

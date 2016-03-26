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

# Serializer to only show limited data on game/review
class GenreLimitSerializer(serializers.HyperlinkedModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    class Meta:
        model = Genre
        fields = [ 'genre', 'url']

    def get_genre(self,obj):
        return obj.get_genre_display()

# Serailzier for to show all data when linked is pressed
class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

# Serializer to only show limited data on game/review
class PlatformLimitSerializer(serializers.HyperlinkedModelSerializer):
    platform = serializers.PrimaryKeyRelatedField(queryset=Platform.objects.all())
    class Meta:
        model = Platform
        fields = [ 'platform', 'url']

# Serailzier for to show all data when linked is pressed
class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

# Serializer to only show limited data on game/review
class DeveloperLimitSerializer(serializers.HyperlinkedModelSerializer):
    developer = serializers.PrimaryKeyRelatedField(queryset=Developer.objects.all())
    class Meta:
        model = Developer
        fields = [ 'developer', 'url']

# Serializer that displayus infrmation about reviews
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['username']

# Serializer that shows all video games
class VideoGameSerializer(serializers.HyperlinkedModelSerializer):
    platform = PlatformLimitSerializer(read_only=False)
    developer =  DeveloperLimitSerializer()
    genre = GenreLimitSerializer()

    class Meta:
        model = VideoGame
        fields = [ "title", "description", "brief",
                    "genre", "platform", "developer", 
                    "rating"]

    def create(self, validated_data):
        print(validated_data.get("owner"))
        game_data = VideoGame.objects.create(
                title=validated_data.get("title"),
                description=validated_data.get("description"),
                brief=validated_data.get("brief"),
                genre=validated_data.get("genre")['genre'],
                platform=validated_data.get("platform")['platform'],
                developer=validated_data.get("developer")['developer'],
                rating=validated_data.get("rating"),
                owner=validated_data.get("owner"),
        )
        return game_data
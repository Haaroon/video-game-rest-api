from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=50, unique=True, primary_key=True)

    def __str__(self):
        return self.genre

class Platform(models.Model):
    platform = models.CharField(max_length=50, unique=True, primary_key=True)

    def __str__(self):
        return self.platform

class Publisher(models.Model):
    publisher = models.CharField(max_length=150, unique=True, primary_key=True)

    def __str__(self):
        return self.publisher

class Developer(models.Model):
    developer = models.CharField(max_length=150, unique=True, primary_key=True)

    def __str__(self):
        return self.developer

class Rating(models.Model):
    rating = models.CharField(max_length=3, unique=True, primary_key=True)

    def __str__(self):
        return self.rating

class MaxPlayers(models.Model):
    maxPlayers = models.CharField(max_length=4, unique=True, primary_key=True)

    def __str__(self):
        return self.maxPlayers

class AgeRating(models.Model):
    ageRating = models.CharField(max_length=3, unique=True, primary_key=True)

    def __str__(self):
        return self.ageRating

class VideoGame(models.Model):
    title  = models.CharField(max_length=100, blank=False, unique=True, primary_key=True)
    description = models.CharField(max_length=1000, blank=False, default='No description')
    brief = models.CharField(max_length=200, blank=False, default='No brief')
    genre = models.ForeignKey(Genre, blank=True, default=None)
    platform = models.ForeignKey(Platform, blank=True, default=None)
    publisher = models.ForeignKey(Publisher, blank=True, default=None)
    developer = models.ForeignKey(Developer, blank=True, default=None)
    rating = models.ForeignKey(Rating, blank=True, default=None)
    maxPlayers = models.ForeignKey(MaxPlayers, null=True, blank=True, default=None)
    ageRating = models.ForeignKey(AgeRating, null=True, blank=True, default=None)
    hasMultiplayer = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='videogames', blank=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def on_success(self):
        return dict(
            id=self.id, 
            title=self.title, 
            description=self.description,
            brief=self.brief,
            genre=self.genre.__str__(),
            platform=self.platform.__str__(),
            publisher=self.publisher.__str__(),
            developer=self.developer.__str__(),
            rating=self.rating.__str__(),
            maxPlayers=self.maxPlayers.__str__(),
            hasMultiplayer=self.has_multiplayer,
            ageRating=self.ageRating.__str__(),
            owner=self.owner.username,
            )

class Review(models.Model):
    username = models.ForeignKey('auth.User', related_name='user', blank=True)
    game = models.ForeignKey(VideoGame, blank=True, default=None, related_name='videogame')
    rating = models.ForeignKey(Rating, default=None, blank=True, related_name='score')
    heading = models.CharField(max_length=40, blank=False, primary_key=True) 
    body = models.CharField(max_length=300, blank=False, default=" ")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading
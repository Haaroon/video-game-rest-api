from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.genre

class Platform(models.Model):
    platform = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.platform

class Publisher(models.Model):
    publisher = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.publisher

class Developer(models.Model):
    developer = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.developer

class Rating(models.Model):
    rating = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.rating

class VideoGame(models.Model):
    title  = models.CharField(max_length=100, blank=False, default='-unknown-')
    description = models.CharField(max_length=1000, blank=False, default='No description')
    brief = models.CharField(max_length=200, blank=False, default='No brief')
    genres = models.ForeignKey(Genre, blank=True, default=None)
    platforms = models.ForeignKey(Platform, blank=True, default=None)
    publishers = models.ForeignKey(Publisher, blank=True, default=None)
    developers = models.ForeignKey(Developer, blank=True, default=None)
    rating = models.ForeignKey(Rating,blank=True, default=None)
    release_date = models.DateTimeField(auto_now_add=True, blank=True)
    owner = models.ForeignKey('auth.User', related_name='videogames', blank=True)

    class Meta:
        ordering = ('release_date',)

    def __str__(self):
        return self.title

    def as_json(self):
        return dict(
            id=self.id, 
            title=self.title, 
            description=self.description,
            brief=self.brief,
            genres=self.genres.__str__(),
            platforms=self.platforms.__str__(),
            publishers=self.publishers.__str__(),
            developers=self.developers.__str__(),
            rating=self.rating.__str__(),
            owner=self.owner.username,
            )
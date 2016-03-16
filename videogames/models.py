from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=50, unique=True)

class Platform(models.Model):
    platform = models.CharField(max_length=50, unique=True)

class Publisher(models.Model):
    publisher = models.CharField(max_length=150, unique=True)

class Developer(models.Model):
    developer = models.CharField(max_length=150, unique=True)

class Rating(models.Model):
    rating = models.CharField(max_length=3, unique=True)

class VideoGame(models.Model):
    title  = models.CharField(max_length=100, blank=False, default='-unknown-')
    description = models.CharField(max_length=1000, blank=False, default='No description')
    brief = models.CharField(max_length=200, blank=False, default='No brief')
    genres = models.ManyToManyField(Genre)
    platforms = models.ManyToManyField(Platform)
    publishers = models.ManyToManyField(Publisher)
    developers = models.ManyToManyField(Developer)
    rating = models.ForeignKey(Rating, )
    release_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ('release_date',)
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=50, unique=True, primary_key=True)

    def __str__(self):
        return self.genre

class Platform(models.Model):
    CONSOLE_CHOICES = (
        (1, 'Console'),
        (2, 'Handheld'),
        (3, 'Mobile'),
        (4, 'PC'),
    )
    platform = models.CharField(max_length=50, unique=True, primary_key=True)
    manufactorer = models.CharField(max_length=50, default="Unknown")
    consoleType = models.IntegerField(choices=CONSOLE_CHOICES, default=1)

    def __str__(self):
        return self.platform

class Developer(models.Model):
    MARKET_CHOICES = (
        (1, 'Worldwide'),
        (2, 'Regional'),
        (3, 'Country'),
    )
    developer = models.CharField(max_length=150, unique=True, primary_key=True)
    headquarters = models.CharField(max_length=100)
    market = models.IntegerField(choices=MARKET_CHOICES, default=1)


    def __str__(self):
        return self.developer

class VideoGame(models.Model):
    title  = models.CharField(max_length=100, blank=False, unique=True, primary_key=True)
    brief = models.CharField(max_length=200, blank=False, default='No brief')
    description = models.CharField(max_length=1000, blank=False, default='No description')
    owner = models.ForeignKey('auth.User', related_name='videogames', blank=True)
    genre = models.ForeignKey(Genre)
    platform = models.ForeignKey(Platform)
    developer = models.ForeignKey(Developer)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def on_success(self):
        return dict(
            id=self.id, 
            title=self.title, 
            brief=self.brief,
            description=self.description,
            owner=self.owner.username,
            genre=self.genre.__str__(),
            platform=self.platform.__str__(),
            developer=self.developer.__str__(),
            )

class Review(models.Model):
    username = models.ForeignKey('auth.User', related_name='user', blank=True)
    RATING_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    heading = models.CharField(max_length=40, blank=False, primary_key=True) 
    body = models.CharField(max_length=300, blank=False, default=" ")
    date_posted = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(VideoGame, related_name='games', blank=False)

    def __str__(self):
        return self.heading

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from videogames import views
from rest_framework import routers

urlpatterns = [
    url(r'^game-list/$', views.VideoGameList.as_view(), name="game-list"),
    url(r'^game-detail/(?P<pk>[0-9]+)/$', views.VideoGameDetail.as_view(), name="game-detail"),
    url(r'^genres/$', views.GenreList.as_view(), name="genres"),
    url(r'^users/$', views.UserList.as_view(), name="user-list"),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name="user-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
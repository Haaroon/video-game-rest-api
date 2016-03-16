from django.conf.urls import url
from videogames import views

urlpatterns = [
    url(r'^all/$', views.videogame_list),
    url(r'^game_detail/(?P<pk>[0-9]+)/$', views.videogame_detail),
]
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from videogames import views

urlpatterns = [
    url(r'^all/$', views.videogame_list),
    url(r'^game_detail/(?P<pk>[0-9]+)/$', views.videogame_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
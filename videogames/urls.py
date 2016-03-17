from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from videogames import views
from rest_framework import routers
from videogames.views import *
from rest_framework import renderers

genres_list = GenreViewSet.as_view({
    'get': 'list',    
})

games = VideoGameViewSet.as_view({
    'get': 'list',
    # 'post': 'create'
})
game_detail = VideoGameViewSet.as_view({
    'get': 'retrieve',
    # 'put': 'update',
    # 'patch': 'partial_update',
    # 'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    # url(r'^$', api_root),
    url(r'^games/$', games),#, name="games"),
    url(r'^game-detail/(?P<pk>[0-9]+)/$', game_detail),#, name="game-detail"),
    url(r'^genres/$', genres_list),#, name="genres_list"),
    url(r'^users/$', user_list),#, name="user-list"),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail),#, name="user-detail"),
])
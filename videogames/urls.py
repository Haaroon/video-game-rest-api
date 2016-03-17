from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from videogames import views
from rest_framework import routers
from videogames.views import *
from rest_framework import renderers

genre_list = GenreViewSet.as_view({
    'get': 'list',    
})

platform_list = PlatformViewSet.as_view({
    'get': 'list',    
})

publisher_list = PublisherViewSet.as_view({
    'get': 'list',    
})

developer_list = DeveloperViewSet.as_view({
    'get': 'list',    
})

rating_list = RatingViewSet.as_view({
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
    url(r'^genres/$', genre_list),
    url(r'^games/$', games),
    url(r'^game-detail/(?P<pk>[0-9]+)/$', game_detail),
    url(r'^users/$', user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail),
])
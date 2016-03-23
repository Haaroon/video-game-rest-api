from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from videogames import views
from rest_framework import routers
from videogames.views import *
from rest_framework import renderers


# games = VideoGameViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
#     'delete': 'destroy'
# })

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

# specific_view = UserViewSet.as_view({
#     'get': 'retrieve'
# })

urlpatterns = format_suffix_patterns([
    # url(r'^games/$', games),
    url(r'^users/$', user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail),
])
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from videogames import views

urlpatterns = [
    url(r'^all/$', views.VideoGameList.as_view()),
    url(r'^game_detail/(?P<pk>[0-9]+)/$', views.VideoGameDetail.as_view()),
    url(r'^genres/$', views.GenreList.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
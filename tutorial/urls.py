from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views
from django.conf.urls import include
from videogames import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'videogames', views.VideoGameViewSet)
router.register(r'genres', views.GenreViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
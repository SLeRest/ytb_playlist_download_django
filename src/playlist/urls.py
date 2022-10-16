from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from playlist import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
#router.register(r'songs', views.SongViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'song', views.SongViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    re_path(r'^ytb-playlist-download/api/0.0/', include(router.urls))
]

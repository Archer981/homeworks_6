from rest_framework import routers

from users.views import LocationViewSet

location_router = routers.SimpleRouter()
location_router.register('', LocationViewSet)
location_patterns = location_router.urls

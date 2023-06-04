from rest_framework import routers

from ads.views.selection import SelectionViewSet

selection_router = routers.SimpleRouter()
selection_router.register('', SelectionViewSet)
selection_patterns = selection_router.urls

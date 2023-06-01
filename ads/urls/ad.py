from django.contrib import admin
from django.urls import path
from rest_framework import routers

from ads.views.ad import *

ad_patterns = [
    # path('', AdViewSet.as_view()),
    # path('create/', AdCreateView.as_view()),
    # path('<int:pk>/', AdDetailView.as_view()),
    # path('<int:pk>/update/', AdUpdateView.as_view()),
    # path('<int:pk>/delete/', AdDeleteView.as_view()),
    path('<int:pk>/upload_image/', AdUploadImageView.as_view()),
]
ad_router = routers.SimpleRouter()
ad_router.register('', AdViewSet)
ad_patterns += ad_router.urls

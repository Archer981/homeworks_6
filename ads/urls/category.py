from django.contrib import admin
from django.urls import path
from rest_framework import routers

from ads.views.category import *

router = routers.SimpleRouter()
router.register('', CategoryViewSet)

category_patterns = [
    # path('', CategoryListView.as_view()),
    # path('create/', CategoryCreateView.as_view()),
    # path('<int:pk>/', CategoryDetailView.as_view()),
    # path('<int:pk>/update/', CategoryUpdateView.as_view()),
    # path('<int:pk>/delete/', CategoryDeleteView.as_view()),
]
category_patterns += router.urls

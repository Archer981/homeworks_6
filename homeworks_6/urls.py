"""
URL configuration for homeworks_6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ads import views
from ads.urls.ad import ad_patterns
from ads.urls.category import category_patterns
from ads.urls.selection import selection_patterns
from homeworks_6 import settings
from users.urls.location import location_patterns
from users.urls.user import user_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ad/', include(ad_patterns)),
    path('selection/', include(selection_patterns)),
    path('cat/', include(category_patterns)),
    path('user/', include(user_patterns)),
    path('location/', include(location_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

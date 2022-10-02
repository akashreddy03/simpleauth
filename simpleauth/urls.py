from django.contrib import admin
from django.urls import path
from base import urls
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls))
]

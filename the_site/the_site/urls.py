
from django.contrib import admin
from django.urls import path, include
from b1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('b1.urls')),
]

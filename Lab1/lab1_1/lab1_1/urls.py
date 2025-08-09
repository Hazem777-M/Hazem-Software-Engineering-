from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('Users.urls')),
    path('logos/', include('logos.urls')),
    path('icons/', include('Icons.urls')),
    path('', lambda request: redirect('users/')), 
]

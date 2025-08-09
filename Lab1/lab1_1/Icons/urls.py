from django.urls import path
from .views import index, about  # Make sure to import the new 'about' function

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'), # This is the new path you need to add
]
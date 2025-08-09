from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),#the first page
    path('students/', views.index, name='index'),
    path('delete/', views.delete_student, name='delete_student'),
    path('update/', views.update_student, name='update_student'),
    path('show/', views.Show, name='show'),
    path('show_fillters/', views.show_fillters, name='show_fillters'),
    path('check/<int:id>/', views.check_age, name='check_age'),

]
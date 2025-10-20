from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello_world, name='hello_world'),
    path('hello/<str:name>/', views.hello_name, name='hello_name'),
]
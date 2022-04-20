from django.urls import path
from . import views

urlPatterns = [
  path('', views.post_list, name='post_list'),
]
from django.urls import URLPattern, path
from . import views

URLPatterns = [
  path('', views.posts_list, name='post_list'),
]
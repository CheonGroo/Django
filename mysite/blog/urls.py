from django.http import HttpRequest, HttpResponse
from django.urls import include, path
from django.views.generic import ListView

from . import views
from . import models

app_name = 'blog'

urlpatterns = [
    path('', views.index),
    path('post_list/', views.post_list, name = 'list'),
    path('post_detail/<int:pk>/', views.post_detail, name = 'detail'),
    path('post_create/', views.post_create, name = 'create'),
]
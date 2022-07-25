from django.http import HttpRequest, HttpResponse
from django.urls import include, path
from django.views.generic import ListView

from . import views
from . import models

urlpatterns = [
    path('', views.index),
    path('post_list/', views.post_list),
    path('post_detail/<int:pk>/', views.post_detail),
    path('post_create/', views.post_create, name="create")
]
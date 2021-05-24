from django.urls import path
from . import views

urlpatterns = [
    path('add', views.index),
    path('show', views.add2),
    path('show2', views.add3),
]
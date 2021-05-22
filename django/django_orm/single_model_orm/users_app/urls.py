from django.urls import path     
from . import views
urlpatterns = [
    path('show', views.index),	 
    path('add', views.adding_users),  
]
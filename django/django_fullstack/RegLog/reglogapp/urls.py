from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index),
    path('reg', views.regestration),
    path('log', views.login),
    path('welcome', views.welcome),
    path('logout', views.logout),
]
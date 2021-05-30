from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('logout', views.logout),
    path('login', views.login),
    path('loginzz', views.loginzz),
    path('indexzz', views.indexzz),
    path('addmessage/<int:id>', views.addmessage),
    path('addcomment/<int:id_message>/<int:id_user>', views.addcomment),
    # path('login/wall', views.wall),
    path('welcome', views.welcome),
]

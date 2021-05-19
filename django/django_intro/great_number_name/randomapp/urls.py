from django.urls import path     
from . import views
urlpatterns = [
    path('', views.indexes),	
    path('number', views.randInt),
    
]
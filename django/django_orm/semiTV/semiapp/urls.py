from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('edit/<int:id>', views.edit)
]
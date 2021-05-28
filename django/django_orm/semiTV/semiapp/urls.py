
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows/new', views.addshow),
    path('add', views.add),
    path('shows', views.ALLshowss),
    path('show/<int:id>', views.TVshow ),
    path('shows/<int:id>/edit',views.edit),
    path('delete/<id>', views.deleteid),
    path('edit/<id>', views.updateshow)
]
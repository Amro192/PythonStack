from django.urls import path, include           # import include
urlpatterns = [
    path('', include('gold_app.urls')),
]

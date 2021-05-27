from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index),
    path('books', views.books_view),
    path('books/<int:id>', views.showbooks),
    path('books/booksadd/<int:book_id>',views.booksadd),
    path('authors' , views.authors),
    path('reauthors',views.authors_view),
    path('authors/<int:id>', views.showauthors),
    path('authors/authorsadd',views.authorsadd),
    
    
]
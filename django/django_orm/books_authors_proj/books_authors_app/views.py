from books_authors_app.models import create_book
from django.shortcuts import redirect, render
from .models import*

def index(request):
    context={'all_books' : allbooks()}

    return render (request,'index.html',context)

def books_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        new_create_book = create_book(title,desc)
    return redirect('/')

def showbooks(request,id):
    book_id = id
    context={'thisBook': getBook(book_id) , 'all_authors': allAuthors()}
    return render(request,'book_view.html' , context)  

def booksadd(request,book_id):
    selecte_id = request.POST['selected_author']
    selecte_author=Authors.objects.get(id=selecte_id)
    this_book = Books.objects.get(id=book_id) 
    this_book.publishers.add(selecte_author)
    return redirect (f'/books/{book_id}')

def authors(request):
    context={'all_authors': allAuthors() }
    return render(request, 'author.html', context)

def authorsadd(request):
    if request.method == 'POST':
        first_name = request.POST['first']
        last_name = request.POST['last']
        notes = request.POST['notes']
        new_create_author =create_author(first_name,last_name,notes)
    return redirect('/authors')    

def authors_view(request,author_id):
    selected_id = request.POST['selected_book']
    selecte_author=Authors.objects.get(id=selected_id)
    this_author = Authors.objects.get(id=author_id) 
    this_author.author.add(selecte_author)
    return redirect (f'/authors/{author_id}')

def showauthors(request,id):
    author_id = id
    context={ 'thisAuthor':getAuthor(author_id) , 'all_books':allbooks()}
    return render(request,'authors_views.html' , context) 


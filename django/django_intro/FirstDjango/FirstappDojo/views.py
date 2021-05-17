from django.shortcuts import redirect ,render , HttpResponse 

def root_method(request):
    return HttpResponse("HELLO")

def root(request):
    return redirect('/blogs')
    
def index(request):
    return  HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return  HttpResponse("placeholder to later display a list of all blogs")

def create(request):
    return redirect('/')

def show(request,num):
    return HttpResponse(f"placeholder to later display a list of all blogs {num}")

def edit(request,num):
    return HttpResponse(f"placeholder to edit blog {num}")

def destroy(request,num):
    return redirect('/blogs')
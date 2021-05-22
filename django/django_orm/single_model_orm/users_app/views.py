from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import users

def index(request):
    context = {
    "all_the_users": users.objects.all() ,

    }
    return render(request, "index.html", context)

def adding_users(request):
    newly_created_user = users.objects.create(first_name=request.POST['firstname'],
    last_name=request.POST['lastname'],
    email_address=request.POST['email'],
    age=request.POST['age'])

    return redirect('/show')

    # "first_name":request.POST['firstname'],
    # 'last_name':request.POST['lastname'],
    # 'age': request.POST['age']
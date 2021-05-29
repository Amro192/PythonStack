from django.shortcuts import redirect, render
from django.contrib import messages
from .models import*

from reglogapp import models

def index (request):
    return render(request,'index.html')

def registration_validation (post_data):
    return models.registration_validation(post_data)

def login_validator(post_data):
    return models.login_validator(post_data)


def regestration(request):
    if request.method == 'POST':   
        first_name=request.POST['first']
        last_name=request.POST['last']
        email=request.POST['email']
        password=request.POST['passwod'] 
        confirm_password=request.POST['cpw']
        errors = models.registration_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        user = create_user(first_name, last_name,email,password)
        request.session['id'] = user.id
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
    return redirect('/welcome')

def login(request):
    if request.method == 'POST': 
        logemail=request.POST['email']
        logpassword=request.POST['passwod']
        errors = login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        user = get_user(logemail, logpassword)
        if user: 
            request.session['id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            return redirect ('/welcome')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def welcome(request):
    if 'first_name' not in request.session:
        return redirect('/')
    return render (request,'welcome.html')
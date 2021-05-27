from semiapp.models import TV, add_show
from django.shortcuts import redirect, render
from . import models

def index(request):
    return render(request,'index.html')

def add(request):
    Title=request.GET['title']
    Network=request.GET['net']
    Release_date=request.GET['release']
    Description=request.GET['desc']
    x = add_show(Title,Network,Release_date,Description)
    y=x.id
    return redirect('/edit' + str(y))

def edit(request):
    context={
        'current_show':TV.objects.get(id=id)
        'id': id
    }
    return render (request, 'tv_show.html',context)

def id(request,id):
    context={
        'id': id
    }

from django.shortcuts import redirect, render
from . import models
from .models import *
from django.contrib import messages


def index(request):
    return render(request,'index.html')

def addshow(request):
    return redirect ('/')

def add(request):
    if request.method == 'POST':    
        Title=request.POST['title']
        Network=request.POST['net']
        Release_date=request.POST['release']
        Description=request.POST['desc']
        addingshow = add_show(Title,Network,Release_date,Description)
    return redirect('/shows')

def TVshow(request,id):
    context={'current_show':TV.objects.get(id=id), 'allshows':AllShowsmodels()}
    return render(request, 'tv_show.html',context)

def ALLshowss(request):
    context={'allshows':AllShowsmodels()}
    return render(request,'Allshow.html',context)


def edit(request,id):
    context={
        'current_show':TV.objects.get(id=id)
    }
    return render (request, 'editshow2.html',context)

def updateshow(request,id):
    # if request.method == 'POST':
    #     Title=request.POST['title']
    #     Network=request.POST['net']
    #     Release_date=request.POST['release']
    #     Description=request.POST['desc']
    # updateshows(id,Title,Network,Release_date,Description)

    errors = TV.objects.strc_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str(id)+'/edit')
    else:
        blog = TV.objects.get(id = id)
        blog.Title = request.POST['title']
        blog.Network = request.POST['net']
        blog.Description = request.POST['desc']
        blog.save()
        updateshows(request.POST['title'], request.POST['net'],request.POST["release"], request.POST['desc'])
        messages.success(request, "Show successfully updated")
    return redirect ('/shows')



def deleteid(request,id):
    DeleteId(id)
    return redirect ('/shows')











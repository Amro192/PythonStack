
from django.db import models

class BlogManager(models.Manager):
    def strc_validator(self, postData):
        errors = {}
        
        if len(postData['title']) < 2:
            errors["title"] = "Show Title should be at least 2 characters"
        if len(postData['net']) < 3:
            errors["net"] = "Show Network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Show Description should be at least 10 characters"
        return errors

class TV(models.Model):
    Title=models.CharField(max_length=255)
    Network=models.CharField(max_length=255)
    Release_date= models.DateField()
    Description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = BlogManager() 

def add_show(Title,Network,Release_date,Description):
    return TV.objects.create(Title=Title,Network=Network,Release_date=Release_date,Description=Description)

def AllShowsmodels():
    tvshow = TV.objects.all()
    return tvshow

def DeleteId(id):
    show = TV.objects.get(id=id)
    show.delete()

def updateshows(id,Title,Network,Release_date,Desciption):
    updatetheshow=TV.objects.get(id=id)
    updatetheshow.Title=Title
    updatetheshow.Network=Network
    updatetheshow.Release_date=Release_date
    updatetheshow.Desciption=Desciption
    updatetheshow.save()

def erorr(postData):
    return TV.objects.strc_validator(postData)

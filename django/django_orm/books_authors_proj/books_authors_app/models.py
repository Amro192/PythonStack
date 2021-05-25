from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ManyToManyField

class Books(models.Model):

    title=models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Authors(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    author = models.ManyToManyField(Books, related_name=('publishers'))
    notes = models.TextField(max_length=255,default="")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

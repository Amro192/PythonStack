from django.db import models

class TV(models.Model):
    Title=models.CharField(max_length=255)
    Network=models.CharField(max_length=255)
    Release_date= models.DateField()
    Description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

def add_show(Title,Network,Release_date,Description):
    return TV.objects.create(Title=Title,Network=Network,Release_date=Release_date,Description=Description)
    
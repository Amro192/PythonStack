from django.db import models

class dojos (models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

class ninjas (models.Model):
    first_name = models.CharField(max_length=255) 
    dojo = models.ForeignKey(dojos, related_name="the_dojos", on_delete = models.CASCADE)
    last_name = models.CharField(max_length=255)


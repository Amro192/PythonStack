from django.core.checks import messages
from django.db import models
from django.db.models.fields import EmailField
import bcrypt
import re	


class userManager(models.Manager):
    def basic_validator(self, postData):       
        errors = {} 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):              
            errors['email'] = "Invalid email address!"



        if len(postData['fname']) < 2:
            errors["fname"] = "fist name should be at least 2 characters"
            
        if len(postData['Lname']) < 2:
            errors["Lname"] = " last should be at least 5 characters"
        
            
        if len(postData['Password']) < 8:
            
            errors["Password"] = "password  should be at least 8 characters"
        return errors
       
        


class user(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)   
    password= models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=userManager() #dose not have to be named specifically



class messsages(models.Model):
    messages = models.TextField()
    user_id=models.ForeignKey(user, related_name="messsage", on_delete = models.CASCADE)
    creat_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

class comments(models.Model):
    comment = models.TextField()
    message_id=models.ForeignKey(messsages, related_name="comments", on_delete = models.CASCADE)
    user_id=models.ForeignKey(user, related_name="comments", on_delete = models.CASCADE)
    creat_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    


def create_user(first_name, last_name, email, password):
    return user.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)

def get_user(email):
    users = user.objects.filter(email=email)
    if len(users)>0:
        print("after if state")
        return users[0]
    return None


def error(post):
    x=user.objects.basic_validator(post)
    return x

def messageadd(messegee, id):
    userx=user.objects.get(id=id)
    messagex= messsages.objects.create(messages=messegee, user_id=userx)
    return messagex

def get_message():
    return messsages.objects.all().order_by("-creat_at")

def addcomment(comment,id_mas,id_user):
    users=user.objects.get(id=id_user)
    mess=messsages.objects.get(id=id_mas)
    comment= comments.objects.create(comment=comment,user_id=users,message_id=mess)
    return comment

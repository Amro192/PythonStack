from django.shortcuts import render, HttpResponse, redirect
from . import models
import bcrypt


def index(request):
    request.session['bool']=False
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        error=models.error(request.POST)
        if len(error)>0:
            request.session['bool']=True
            context = {
            'error': error
             }
            return render(request, 'index.html',context)
        
        first_name = request.POST['fname']
        last_name = request.POST['Lname']
        email = request.POST['email']
        password = request.POST['Password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()    
        print(pw_hash)
        conpassword = request.POST['confpass']
        if password == conpassword:
            user = models.create_user(first_name, last_name, email, pw_hash)
            request.session['id'] = user.id 
            request.session['first_name'] = user.first_name 
            request.session['last_name'] = user.last_name
            return redirect("/welcome")
    return redirect("/")

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['Password']
        user = models.get_user(email)
        if user:
            request.session['id'] = user.id 
            request.session['first_name'] = user.first_name 
            request.session['last_name'] = user.last_name
            if user:
                logged_user = user
                if bcrypt.checkpw(request.POST['Password'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
                    return redirect("/welcome")
            # never render on a post, always redirect!
            
    return redirect('/')


def loginzz(request):
    return render(request, "login.html")
                    
def indexzz(request):
    return render(request, "index.html")

def addmessage(request,id):
    if request.method=='POST':
        message=request.POST['message']
        messagex=models.messageadd(message,id)
        return redirect("/welcome")

def addcomment(request,id_message,id_user):
    if request.method=='POST':
        comment=request.POST['comment']
        messagex=models.addcomment(comment,id_message,id_user)
        return redirect("/welcome")

# def wall(request):
#     context={
#         'messages':models.get_message()
#     }
#     return render(request,"welcome.html",context)

def welcome(request):
    context={
    'messages':models.get_message()
    }
    return render(request, "welcome.html",context)


from dojo_ninjas_app.models import dojos, ninjas
from django.shortcuts import redirect, render,HttpResponse

def index(request):
        context = {
            "all_dojos": dojos.objects.all() ,
            "all_ninjas": ninjas.objects.all(),
            "dojo": dojos.objects.all()
            }
        return render(request, "index.html", context)


def add2(request):
    newly_created_dojo = dojos.objects.create(
    name=request.POST['name'],
    city=request.POST['city'],
    state=request.POST['state'])
    return redirect('/add')

def add3(request):
    print(request.POST)
    newly_created_ninjas = ninjas.objects.create(
    first_name=request.POST["first_name"],
    last_name=request.POST["last_name"],
    dojo= dojos.objects.get(id=request.POST["selects"]))
    return redirect('/add')


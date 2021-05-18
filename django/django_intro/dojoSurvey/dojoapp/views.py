from django.shortcuts import redirect, render

def index(request):
    return render(request,"index.html")

def dojoooo(request):
    
    if request.method == "GET":
        print("a GET request is being made to this route")
        return render(request, "results.html")

    if request.method == "POST":
        
        request.session['namee']= request.POST["namee"]
        request.session['dojoo'] = request.POST["dojoo"]
        request.session['languagee'] = request.POST["languagee"]
        request.session['comments'] = request.POST["comments"]
        return redirect("/results")

def redirectee(request):
    print(request.POST)
    return render(request,"results.html")

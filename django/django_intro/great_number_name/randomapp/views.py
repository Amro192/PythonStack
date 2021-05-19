from django.shortcuts import redirect, render
import random


def indexes(request):
    return render(request,"index.html")

def randInt(request,min =0, max=100):
    
    if request.method == "POST":
        
        if 'num1' not in request.session:
            request.session['num1'] =round(random.random()*(max-min))
        else: pass
        request.session['num2'] = int(request.POST['num2'])

        print(request.POST['num2'])
        print(request.session['num2'])
        print(request.session['num1'])


        if request.session['num2'] == request.session['num1']:
            request.session['flag'] = 1
            del request.session['num1']
        elif  request.session['num2'] > request.session['num1']:
            request.session['flag'] = 2
        elif  request.session['num2'] < request.session['num1']:
            request.session['flag'] = 3

            


    return render(request,'low.html')

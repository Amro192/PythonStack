from django.shortcuts import render, redirect
from datetime import datetime
import random 
def index(request):
    if "your_gold" not in request.session or "activate" not in request.session:
        request.session['your_gold']= 0 
        request.session['activate']= []
    return render(request, "index.html")


def amount_mony(request):
    if request.method == 'POST' :
        if request.POST['bild']== 'Farm':
            gold= random.randint(10,20)
            request.session['activate'].append('you are earndep' + str(gold))

        elif request.POST['bild'] == 'Cave':
            gold= random.randint(5,10)
            request.session['activate'].append('you area earnde' + str(gold) )

        elif request.POST['bild'] == 'House':
            gold= random.randint(2,5)
            request.session['activate'].append('you arew earnde' + str(gold) )

        elif request.POST['bild'] == 'Casino':
            gold= random.randint(-50,50)
            if gold >=0:
                request.session['activate'].append('you are earnde' + str(gold) )

            else:
                request.session['activate'].append('you are  earnde ' + str(gold) )
        request.session['your_gold'] += gold
            
    return redirect('/')        
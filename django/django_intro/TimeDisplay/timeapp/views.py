from django.shortcuts import render ,HttpResponse
from time import gmtime, localtime, strftime
    
def index(request):
    context = {
    "time": strftime("%b %d, %Y ", localtime()),
    "time2":strftime("%H:%M %p ", localtime())
    }
    return render(request,'index.html', context)


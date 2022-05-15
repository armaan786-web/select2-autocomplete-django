from django.shortcuts import render
from app .models import *

# Create your views here.
def displaycolor(request):
    displaycolor = displaydd1.objects.all()
    context = {
        'color':displaycolor
    }
    return render(request,"home.html",context)



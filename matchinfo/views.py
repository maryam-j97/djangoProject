from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def Home(request):
    home = Hometeam.objects.all()
    away = Awayteam.objects.all()
    context={'home':home,'away':away}
    return render(request, "./match.html",context)

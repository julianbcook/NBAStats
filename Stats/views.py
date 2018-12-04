# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse
from .models import Player

def index(request):
    return render(request, 'Stats/index.html')
    #return HttpResponse(x)
# Create your views here.
def login(request):
    return render(request,'Stats/login.html')

def register(request):
    return render(request,'Stats/register.html')

def badPage(request):
    return render(request,'Stats/404.html')

def blank(request):
    return render(request,'Stats/blank.html')

def charts(request):
    return render(request,'Stats/charts.html')

def forgot(request):
    return render(request,'Stats/forgot-password.html')

def tables(request):
    all_players = Player.objects.all()
    query = "SELECT 1 id, p_pname, p_age, p_points, p_assists, p_fgp, p_3pp FROM PLAYER"
    q = []
    
    for p in Player.objects.raw(query):
        q.append(p)

    args = {'playerList' : q}
    return render(request,'Stats/tables.html', args)
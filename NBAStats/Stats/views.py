# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'Stats/index.html')
# Create your views here.

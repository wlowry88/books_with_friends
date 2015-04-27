import json
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    context = {
            'Hey': 'Fool'
            }
    return render(request, 'read_with_friends/index.html', context)

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def farm(request):
    return render(request, 'farm.html')

def trails(request):
    return render(request, 'farm.html')

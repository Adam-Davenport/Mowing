from django.shortcuts import render
from django.http import HttpResponseRedirect
from record.models import Mowing

def index(request):
    if request.method == 'POST':
        post_record(request)
        return HttpResponseRedirect('/')
    else:
        records = Mowing.objects.order_by('date').reverse()
        context = {
            'records': records
        }
        return render(request, 'index.html', context)

def post_record(request):
    print(request.POST)
    location = request.POST['location']
    direction = request.POST['direction']
    session = Mowing.objects.create(location=location, direction=direction)
    session.save()

def home(request):
    return render(request, 'home.html')

def farm(request):
    return render(request, 'farm.html')

def trails(request):
    return render(request, 'trails.html')

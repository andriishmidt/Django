from django.shortcuts import render
from .models import Articles, Categories

def index(request):
    notes = Articles.objects.order_by('date')
    return render(request, 'notes/index.html', {'notes': notes})

def about(request):
    categories = Categories.objects.all
    return render(request, 'notes/about.html', {'categories': categories})

from django.shortcuts import render, redirect
from .models import Articles, Category
from .forms import ArticlesForm, CategoryForm
from django.shortcuts import get_object_or_404

def index(request):
    notes = Articles.objects.order_by('-id')
    return render(request, 'notes/index.html', {'notes': notes})

def about(request):
    categories = Category.objects.all()  # Added missing parentheses
    return render(request, 'notes/about.html', {'categories': categories})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма була не коректна'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'notes/create.html', data)

def add_category(request):
    error = ''
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')
        else:
            error = 'Форма була не коректна'

    form = CategoryForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'notes/add_category.html', data)

def delete_note(request, note_id):
    note = get_object_or_404(Articles, id=note_id)
    note.delete()
    return redirect('home')


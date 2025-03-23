from django.shortcuts import render


def index(request):
    data = {
        'title': 'Головна сторінка!',
        'values': ['Some', 'Hello', '12345'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'notes/index.html', data)


def about(request):
    return render(request, 'notes/about.html')

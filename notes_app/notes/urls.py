from django.urls import path
from . import views
from .views import delete_note

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('add_category', views.add_category, name='add_category'),
    path('delete/<int:note_id>/', delete_note, name='delete_note')


]


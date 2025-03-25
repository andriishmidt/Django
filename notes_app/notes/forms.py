from django import forms
from .models import Articles, Category

class ArticlesForm(forms.ModelForm):
    category = forms.ModelChoiceField(  # Changed from 'categories' to 'category'
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Articles
        fields = ['title', 'reminder', 'full_text', 'date', 'category']  # Fixed field name

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва нотатки'}),
            'full_text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст'}),
            'reminder': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Нагадування'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Категорія'}),
        }

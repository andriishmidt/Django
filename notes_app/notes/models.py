from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Changed from 'title' to 'name'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Articles(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    full_text = models.TextField('Текст')
    reminder = models.CharField('Нагадування', max_length=250)
    date = models.DateTimeField('Дата')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Changed 'categories' to 'category'

    def __str__(self):
        return f'Нотатка: {self.title}'

    class Meta:
        verbose_name = 'Нотатка'
        verbose_name_plural = 'Нотатки'


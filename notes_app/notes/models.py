from django.db import models

class Categories(models.Model):
    title = models.CharField('Категорія', max_length=50, unique=True)

    def __str__(self):
        return f'Категорія: {self.title}'

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Articles(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    full_text = models.TextField('Текст')
    reminder = models.CharField('Нагадування', max_length=250)
    date = models.DateTimeField('Дата')
    categories = models.ManyToManyField(Categories, related_name="articles")

    def __str__(self):
        return f'Нотатка: {self.title}'

    class Meta:
        verbose_name = 'Нотатка'
        verbose_name_plural = 'Нотатки'

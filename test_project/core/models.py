from django.db import models

# Create your models here.
class Articles(models.Model):
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата Создания')
    name = models.CharField(max_length=50, verbose_name='Название')
    text = models.TextField(verbose_name='Текст Статьи')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

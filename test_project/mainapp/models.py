from django.db import models


class Post(models.Model):
    """Пост"""
    title = models.CharField('Название', max_length=1024)
    slug = models.SlugField('URL', max_length=1024)
    content = models.TextField('Контент')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

from django.db import models
from django.urls import reverse

# Create your models here.


class Tests(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    formula = models.CharField(max_length=120, verbose_name='Формула')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    indicators = models.CharField(max_length=255, default='', verbose_name='Показатели к тестированию')
    results = models.TextField(blank=True, verbose_name='Таблица результатов')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('test', kwargs={'test_slug': self.slug})

    class Meta:
        verbose_name = 'Тесты' #для отображения в админ панели
        verbose_name_plural = 'Тесты' #для отображения в админ панели без s
        ordering = ['pk']


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(upload_to='news/%Y/%m/%d/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})

    class Meta:
        verbose_name = 'Новости' #для отображения в админ панели
        verbose_name_plural = 'Новости' #для отображения в админ панели без s
        ordering = ['-time_create']
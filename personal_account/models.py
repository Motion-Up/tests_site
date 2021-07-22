from django.contrib.auth.models import User
from tests.models import Tests
from django.db import models

from django.urls import reverse

# Create your models here.


class UserResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователи')
    name_test = models.ForeignKey(Tests, on_delete=models.CASCADE, verbose_name='Название теста')
    results = models.FloatField(verbose_name='Результаты')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата прохождения теста')

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Результаты пользователей' #для отображения в админ панели
        verbose_name_plural = 'Результаты пользователей' #для отображения в админ панели без s
        ordering = ['-time_create']

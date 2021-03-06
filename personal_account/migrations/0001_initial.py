# Generated by Django 3.2.4 on 2021-06-20 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tests', '0003_auto_20210615_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results', models.FloatField(verbose_name='Результаты')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата прохождения теста')),
                ('name_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.tests', verbose_name='Название теста')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователи')),
            ],
            options={
                'verbose_name': 'Результаты пользователей',
                'verbose_name_plural': 'Результаты пользователей',
                'ordering': ['-time_create'],
            },
        ),
    ]

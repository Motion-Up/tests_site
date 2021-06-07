from django.contrib import admin
from .models import *


class TestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Tests, TestsAdmin)

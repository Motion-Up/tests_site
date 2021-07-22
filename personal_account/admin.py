from django.contrib import admin
from .models import *


class UserResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name_test', 'results', 'time_create')


admin.site.register(UserResult, UserResultAdmin)

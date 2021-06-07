from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('test/<slug:test_slug>/', show_test, name='show_test'),
    path('answer/<slug:test_slug>/', answer, name='answer'),
]
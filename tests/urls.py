from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('tests/', all_tests, name='all_tests'),
    path('test/<slug:test_slug>/', show_test, name='show_test'),
    path('answer/<slug:test_slug>/', answer, name='answer'),
    path('news/', all_news, name='all_news'),
    path('news/<slug:news_slug>/', show_news, name='show_news'),
]
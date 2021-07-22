from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('account/', personal_page, name='personal_page'),
]
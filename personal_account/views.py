from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from tests.models import Tests
from .models import *


# Create your views here.


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт успешно создан для {user}')
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'personal_account/register.html', context)


def loginPage(request):
    form = LoginUserForm()

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Неверно введен логин или пароль!')
    context = {
        'form': form
    }
    return render(request, 'personal_account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def personal_page(request):
    tests = Tests.objects.all()
    results = UserResult.objects.all().filter(user=request.user)
    all_results = {}

    for test in tests:
        all_results[test.title] = {}
        test_results = results.filter(name_test=test)

        for number in range(4):
            if len(test_results) >= number + 1:                                     # Проверяем на существование индекс, если есть то записываем результат
                all_results[test.title][test_results[number].time_create] = test_results[number].results
            else:
                all_results[test.title][number + 1] = 0

        #if len(test_results) >= 4:                                                                  # Получаем результаты
        #    all_results[test.title][5] = int(test_results[3].results) - int(test_results[0].results)
        #else:
        #    all_results[test.title][5] = 'Недостаточно данных'

    context = {
        'tests': tests,
        'results': results,
        'all_results': all_results,
    }
    return render(request, 'personal_account/personal_page.html', context)

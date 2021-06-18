from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


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

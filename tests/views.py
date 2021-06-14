from django.http import HttpResponseNotFound, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaulttags import register

from .models import *


# Create your views here.


def index(request):
    tests = Tests.objects.all()
    news = News.objects.all()
    context = {
        'tests': tests,
        'news': news
    }

    return render(request, 'tests/base.html', context=context)


def all_tests(request):
    tests = Tests.objects.all()
    context = {
        'tests': tests,
    }

    return render(request, 'tests/all_tests.html', context=context)

def show_test(request, test_slug):
    post = get_object_or_404(Tests, slug=test_slug)
    indicators = post.indicators.split(',')
    # создали словарь чтобы получить номер для id и индикатор для теста
    dict_indicators = {}
    for i in range(len(indicators)):
        dict_indicators[f'{i}'] = indicators[i]
    context = {
        'post': post,
        'indicators': dict_indicators,
    }

    return render(request, 'tests/show_test.html', context=context)


def answer(request, test_slug):
    post = get_object_or_404(Tests, slug=test_slug)
    formula = post.formula
    indicators = post.indicators.split(',')
    for number in range(len(indicators)):
        formula = formula.replace('number', request.GET.get(f'{number}'), 1)
    try:
        answer = float("{0:.2f}".format(eval(formula)))
        context = {
            'post': post,
            'answer': answer,
            'result': True,
            "error": False,
            'results': post.results.split('.'),
        }
        return render(request, 'tests/show_test.html', context=context)

    except:
        indicators = post.indicators.split(',')
        # создали словарь чтобы получить номер для id и индикатор для теста
        dict_indicators = {}
        for i in range(len(indicators)):
            dict_indicators[f'{i}'] = indicators[i]
        context = {
            'post': post,
            'result': False,
            "error": True,
            'return_test': dict_indicators

        }

        return render(request, 'tests/show_test.html', context=context)


def all_news(request):
    news = News.objects.all()
    context = {
        'news': news,
    }

    return render(request, 'tests/all_news.html', context=context)


def show_news(request, news_slug):
    news = get_object_or_404(News, slug=news_slug)
    context = {
        'news': news
    }

    return render(request, 'tests/show_news.html', context=context)


def pageNotFound(request, exception):

    return HttpResponseNotFound('<h1>Page not found!</h1>')

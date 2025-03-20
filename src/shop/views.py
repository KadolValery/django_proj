from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_views(request,year):
    return HttpResponse(f"<h1>Это главная страница, где будет отображаться информация о сайте и задача сервиса{year}<h/1>")

def second_views(request,year):
    return HttpResponse(f"<h1>Это страница информации где будут в дальнейшем выводиться все товары маркетплейса{year}<h/1>")

def first_html(request):
    data={
        "user":"Ivan",
        "age": 24,
    }

    context={
        "data": data,
        "var_str": "Hello context"
    }

    return render(request, template_name='hello.html',context=context)
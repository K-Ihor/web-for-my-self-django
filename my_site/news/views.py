from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Category


def index(request):  # обязательный аргумент request
    news = News.objects.all()  # .order_by('-created_at')- выведет новости от свежей к старой.  это можно и в моделс.пй указать    #.all()  # хотим посмотреть все новости
    # categories = Category.objects.all()  # хотим вывести категории на страничку objects.all()-указывает на то что нам нужны все категории (убрали из-за того что сделали шаблон сайтбара категории)
    context = {
        'news': news,
        'title':'Список новостей',
        # 'categories': categories, - убрали из-за того что сделали шаблон сайтбара категории
    }
    return render(request, 'news/index.html', context)  # передаем нашь html шаблон

    # res = '<h1>Список новостей</h1>'
    # for item in news:
    #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n' # дописываем res следующими данными
    # # print(dir(request))  # для того чтоб показать инфу в консоле, пока что не ясную моему мозгу
    # return HttpResponse(res)  # возвращать будет http респонс(конструктор данного класса)


# def test(request):
#     return HttpResponse('<h1>Тестовая страничка</h1>')

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)  # получаем определенную колонку из БД
    # categories = Category.objects.all()  # список категорий оставляем чтоб светился в сайт-баре
    category = Category.objects.get(pk=category_id)  # выводим инфу о запрошенной категории и получаем инф по первичному ключу pk=
    return render(request, 'news/category.html', {'news': news, 'category': category})  # , 'categories': categories (убрали из-за того что сделали шаблон сайтбара категории)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)  # сохраняем в переменную конкретную новость
    news_item = get_object_or_404(News, pk=news_id)  # на случай если новость удалена и ссылка на нее уже не работает(обработка исключения)
    return render(request, 'news/view_news.html', {"news_item": news_item})  # передаем, название шаблона который будет рендериться view_news.html в папке new/, и контекст {"..."}










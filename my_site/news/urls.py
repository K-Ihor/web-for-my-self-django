from django.urls import path  # импортируем ф-ю path для построения списков маршрутов

from .views import *  # .- точка указывает на текущую дерикторию

# создаем переменную со списком адресов которые будет формеровать ф-я path
urlpatterns = [
    path('', index, name='home'),  # присваеваем имена ссылкаим name='home'
    #  первым агрументом мы указываем ''- пустую строку в место (news/) так как часть пути отбрасывается, эта часть указана в migration/urls.py при использовании include
    # фторой аргумент ф-я index из текущей дериктории, файла .views
    path('category/<int:category_id>/', get_category, name='category'),  # когда джанго встретит такую ссылку(category/<int:category_id>/) то подключит get_category
    path('news/<int:news_id>/', view_news, name='view_news'),  # когда прописали путь идем создавать ф-ю view_news
]




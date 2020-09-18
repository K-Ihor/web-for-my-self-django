from django.urls import path  # импортируем ф-ю path для построения списков маршрутов

from .views import *  # .- точка указывает на текущую дерикторию

# создаем переменную со списком адресов которые будет формеровать ф-я path
urlpatterns = [
    path('register/', register, name='register'),  # путь для регистра, при указ.маршруте 'register/' вызыв ф-ю register из views
    path('login/', user_login, name='login'),  # путь для регистра, при указ.маршруте 'login/' вызыв ф-ю login из views
    path('logout/', user_logout, name='logout'),  # для выхода с аккаунта
    path('', HomeNews.as_view(), name='home'),  # указываем путь для класса который мы описали в views.py
    # path('', index, name='home'),  # присваеваем имена ссылкаим name='home'
    #  первым агрументом мы указываем ''- пустую строку в место (news/) так как часть пути отбрасывается, эта часть указана в migration/urls.py при использовании include
    # фторой аргумент ф-я index из текущей дериктории, файла .views
    # path('category/<int:category_id>/', get_category, name='category'),  # когда джанго встретит такую ссылку(category/<int:category_id>/) то подключит get_category
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),  # переписыаем наш маршрут получения категорий по созданный класс
                                                            #  extra_context={'title': 'Какой-то тайтл'}), - опционально предаем эту настройку во NewsByCategory.as_view(extra_context={}, name='category')  и ряд других настроек
    # path('news/<int:news_id>/', view_news, name='view_news'),  # когда прописали путь идем создавать ф-ю view_news
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),  # маршрут для созданного класса
    # path('news/add-news/', add_news, name='add_news'),  # добавляем путь для форм в виде фу-ции
    path('news/add-news/', CreateNews.as_view(), name='add_news'),  # добавляем путь для форм в виде класс
    path('test/', test, name='test'),  # тестируем построчную пагинацию, когда будет запрошен адрес test/, мы обратимся к фу-ци test( и отправку письма тоже тестим на этом пути)
]




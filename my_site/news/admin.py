from django.contrib import admin
from .models import News, Category  # Импортируем модель
# Register your models here.


# Класс являеться под класом .ModelAdmin
       # NewsAdmin - настройка(Админки) модели News
class NewsAdmin(admin.ModelAdmin):  # чтоб вывести дополнительные поля из базы в интерфэйс(предтавление модели в админке)
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')  # поля которые мы хотим видеть
    list_display_links = ('id', 'title')  # превращает поля в ссылку(когда наводишь мышкой наименование подсвечивается)
    search_fields = ('title', 'content')  # Поля по которым можно проводить поиск(после обновления появиться поле для поиска)
    list_editable = ('is_published', )  # поле которое мы хотим редактировать
    list_filter = ('is_published', 'category')  # поля по каторым мы хотим фильтровать.

class CategoryAdmin(admin.ModelAdmin):  # настройка модели Category
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)  # если кортэж из одного элемента то обязательно ставим запятую!!!



# порядок регистрации модели важен, сначала пишем основную модель, потом её настроеный момент
admin.site.register(News, NewsAdmin)  # регистрируем нашу модель в админке и Класс NewsAdmin тоже приписываем
admin.site.register(Category, CategoryAdmin)  # Регестрируем еще одну нашу модель



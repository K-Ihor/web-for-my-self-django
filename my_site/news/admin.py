from django.contrib import admin
from django.utils.safestring import mark_safe  # для получения картинки в админке в поле photo
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget  # для подключения редактора текста в админку

from .models import News, Category  # Импортируем модель
# Register your models here.


class NewsAdminForm(forms.ModelForm):  # класс для подключения редактора текста в админку
    content = forms.CharField(widget=CKEditorUploadingWidget())  # поле модели в которое поместим редактор(тело новостей)

    class Meta:
        model = News  # нужная нам модель
        fields = '__all__'


# Класс являеться под класом .ModelAdmin
       # NewsAdmin - настройка(Админки) модели News
class NewsAdmin(admin.ModelAdmin):  # чтоб вывести дополнительные поля из базы в интерфэйс(предтавление модели в админке)
    form = NewsAdminForm  # вносим в админку наш CKEditor
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')  # поля которые мы хотим видеть
    list_display_links = ('id', 'title')  # превращает поля в ссылку(когда наводишь мышкой наименование подсвечивается)
    search_fields = ('title', 'content')  # Поля по которым можно проводить поиск(после обновления появиться поле для поиска)
    list_editable = ('is_published', )  # поле которое мы хотим редактировать
    list_filter = ('is_published', 'category')  # поля по каторым мы хотим фильтровать.
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'updated_at')  #  Указываем список полей которые нам нужны внутри нашей новости
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')  # указываем поля которые только для чтения(их нельзя изменять), после указания этих полей у нас не будет возникать ошибка
    save_on_top = True  # выводим кнопки для сохранения дополнительно сверху админки

    def get_photo(self, obj):  # метод возвращает html код картинки, чтоб в админке выводить в поле фотку
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')  # - помещает в поле html код
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'  #


class CategoryAdmin(admin.ModelAdmin):  # настройка модели Category
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)  # если кортэж из одного элемента то обязательно ставим запятую!!!



# порядок регистрации модели важен, сначала пишем основную модель, потом её настроеный момент
admin.site.register(News, NewsAdmin)  # регистрируем нашу модель в админке и Класс NewsAdmin тоже приписываем
admin.site.register(Category, CategoryAdmin)  # Регестрируем еще одну нашу модель

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'

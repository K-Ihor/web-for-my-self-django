from django.db import models
from django.urls import reverse  # для def get_absolute_url(self):

# Модели сдесь описываються в виде класса(описываем поля базы данных)
# помним что этот клас наследуеться , следовательно это под клас
# Далее мы описываем (свойства,атрибуты,переменные- назыв по разному)класса(то есть поля )
# id не описываем джанго его сам намутит


class News(models.Model):                   # verbose_name='Наитменование' - указывает как будет светиться в админке наше созданное поле
    title = models.CharField(max_length=150, verbose_name='Наитменование')  # указываем title тип поля .CharField и макс.кол. символов max_length=150 как обязательный атрибут
    content = models.TextField(blank=True, verbose_name='Контент')  # blank=True не обязательный атрибут - говорит о том что поле не обязательно к заполнению, а по умолчанию все обязательны к заполнению
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')  # auto_now_add=True - схранит время добавления записи, а если auto_now=True то будет сохранять время изменения записи
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')  # auto_now=True будет сохранять время изменения,обновления записи
                                                                              # blank=True - говорит что поле для заполнения не обязательно
    photo = models.ImageField(upload_to='photos/%Y%m%d/', verbose_name='Фото', blank=True)  # upload_to= - можно указать куда именно загружать файл по указанному пути. photos/%Y%m%d/-означает что фото будут разбиваться в папки по дате
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')  # default=True - если не указать True то по умолчанию None
                                            # on_delete=models.PROTECT - защита от удаления связанных данных в таблице
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', null=True)  # Связываем модели(таблицы) Если 'Category' создаеться позже то указываем её в скобках в виде строки, если раньше то без скобок' '

    def get_absolute_url(self):  # используя этот параметер django сам выстроит ссылку.
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self):  # чтоб выводить данные title в виде строки а не ( News object (1) )
        return self.title

    class Meta:  # для модели News
        verbose_name = 'Новость'  # наименование модели в единственном числе
        verbose_name_plural = 'Новости'  # в множественном числе
        ordering = ['-created_at']  # Указ порядок сортировки


class Category(models.Model):  # после полного создания еще одной модели проделываем миграцию
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')  # db_index=True - индексирует поле(более быстрая возможность до него добраться)

    def get_absolute_url(self):  # используя этот параметер django сам выстроит ссылку.
        return reverse('category', kwargs={"category_id": self.pk})


    def __str__(self):  # чтоб выводить данные title поля категории в виде строки а не ( Сategory object (1) )
        return self.title

    class Meta:  # для модели Category
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']  # Указ порядок сортировки
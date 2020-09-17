from django import forms

# from .models import Category
# #  1) Создаем форму которая не связана с моделью  и пописываем поля в ней
# class NewsForm(forms.Form):                                 # widget=forms.Tex... делает вид поля под бутсрап
#     title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={
#         "class": "form-control",
#         "rows": 5  # сделает вид поля ввода текста меньше
#     }))
#     is_published = forms.BooleanField(label='Опубликовано?', initial=True)
#     category = forms.ModelChoiceField(empty_label='Выберите категорию', label='Категория', queryset=Category.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))

# 2 ) Форма связанная с моделью
from .models import News
import re  # импортируем этот модуль для регулярных выражений.(нам для создания кастомного валидатора)
from django.core.exceptions import ValidationError  # для вывода исключения
from django.contrib.auth.forms import UserCreationForm  # для создания формы регистрации
from django.contrib.auth.models import User  # для создания формы регистрации юзера


class UserRegisterForm(UserCreationForm):  # для создания формы регистрации
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов', widget=forms.TextInput(attrs={"class": "form-control"}))  # Если поставить 'autocomplete': 'off' в attrs, то подсказки ввода выдавать не будет
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))  # определяем поле которое нам нужны
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User  # Связываем форму с моделью User(это джанговская модель)
        fields = ('username', 'email', 'password1', 'password2')  # поля в каком порядке должны быть представлены в форме. И по желанию ('first_name' and 'last_name')
        # widgets = {
        #     'username': forms.TextInput(attrs={"class": "form-control"}),
        #     'email': forms.EmailInput(attrs={"class": "form-control"}),
        #     'password1': forms.PasswordInput(attrs={"class": "form-control"}),
        #     'password2': forms.PasswordInput(attrs={"class": "form-control"}),
        # }  # Лучше настраивать это выше в (class UserRegisterForm(UserCreationForm):) так как имя пользователя настраиваеться, а имэйл и парол нет


class NewsForm(forms.ModelForm):
    class Meta:  # Описываем как должна выглядеть наша форма
        model = News  # указываем с какой моделью связанна наша форма
        # fields = '__all__'  # указывае поля которые которые хотим видеть в форме.('__all__' - все поля из формы) но лучше описать поля как ниже
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):  # создаем кастомный валидатор для формы поля title
        title = self.cleaned_data['title']  # получаем уже очищенные данный пройденные через валидатор модели со словаря формы по ключу title
        if re.match(r'\d', title):  # re.match - метод ищет что-то(цыфру '\d') в начале строки(title). r -ставиться потму что '\d' это эскейп последовательность(лучше ставить перед рег.выраж.)
            raise ValidationError('Название не должно начинаться с цыфры')
        return title





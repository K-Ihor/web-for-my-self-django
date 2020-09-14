class MyMixin(object):  # Mixinn юзаем только для класса, а для ф-ий используют декоратор(login_required() )
    mixin_prop = ''

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, s):
        if isinstance(s, str):  # являеться ли s строкой str
            return s.upper()  # возводит строку в верхний регистр
        else:
            return s.title.upper()  # если это объект(в нашем случае это кверисет) то приводим его обэкт title к верхнему регистру.


# а для ф-ий используют декоратор(login_required() - чтоб ограничить доступ к каким либо функциям и дать разришение только авторизованным пользователям(админу)
# для класса юзают LoginRequired mixin   (в шаблоне будет так выглядеть)
# {% if request.user.is_authenticated %} если прошел аунтефикацию  то покажут ему ссылку добавления новости но доступ по ссылке закрываеть во views.py
# <li class="nav-item"><a class="nav-link" href="{% url 'add_news' %}">Добавить новость</a></li>
# {% endif %}

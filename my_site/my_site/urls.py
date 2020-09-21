"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from news.views import *  # импортируем нашу ф-ю index(которую мы написали)  или(*) все ф-ции из модуля news.views
                              # не забываем указать что my_site - это корневая папка(чтоб не светить ошибку)
                              #  если используем include то (from news.views import * ) ненужно.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('news.urls')),  # указываем новый маршрут при обращении к news/ будет вызвана ф-я index из news.views, а если пустая строка '' то обратиться к инклюд и начальная страничка выведет нашу ф-ю индекс в начальной страничке
    # path('test/', test),  # либо через include(список вложеных маршрутов с нашего созданного файла urls в модуле news)
]


# создаем константу для отладочного режима(режима разработки) чтоб можно было просматривать фото файлы пока DEBUG = True

if settings.DEBUG:  # на реальном сервере это условие выполняться не будет

    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # по этому маршруту в отладочном режиме джанго будет отдавать медео вайлы


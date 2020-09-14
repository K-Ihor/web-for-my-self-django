from django import template
from django.db.models import Count  # для того чтоб убрать из списка категории без записей

from news.models import Category


register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')  # показывает список категорий в левом вергнем углу
def show_categories():
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)  # убераем из списка который выводиться в браузере категорию в которой нет записей
    return {"categories": categories}

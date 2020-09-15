from django import template
from django.db.models import Count, F  # Count - для того чтоб убрать из списка категории без записей

from news.models import Category


register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')  # показывает список категорий в левом вергнем углу
def show_categories():
    # categories = Category.objects.all()
    # categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)  # убераем из списка который выводиться в браузере категорию в которой нет записей
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)  # С помощю filter=F('news__is_published') указываем чтоб возле категорий счет новостей учитывалься только если новость опублекована.
    return {"categories": categories}

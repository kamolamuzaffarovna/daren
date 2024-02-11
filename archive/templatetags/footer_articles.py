from django import template

from archive.models import Article, Category, Tag

register = template.Library()


@register.simple_tag
def site_bar_articles():
    return Article.objects.order_by('-id')[:2]


@register.simple_tag
def article_category():
    return Category.objects.all()


@register.simple_tag
def article_tags():
    return Tag.objects.all()





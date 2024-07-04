from django import template

register = template.Library()


@register.simple_tag
def get_current_languages():
    return ['en', 'ru', 'uz']
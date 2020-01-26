from django import template

register = template.Library()

@register.filter(name='uppercase')
def uppercase(value):

    # ex = 8/0

    return str(value).upper()
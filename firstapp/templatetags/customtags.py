from django import template

register = template.Library()

@register.simple_tag(name='to_list')
def to_list(*args):

    return args
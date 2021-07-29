from django import template
register = template.Library()


@register.filter(name='phone_conversion')
def phone_conversion(number):
    """ (xxx) xxx-xxxx."""
    first = number[0:3]
    second = number[3:6]
    third = number[6:10]
    return '(' + first + ')' + ' ' + second + '-' + third

from django import template

register = template.Library()


@register.filter(name='phone_conversion')
def phone_conversion(number):

    first = number[0:3]
    second = number[3:6]
    third = number[6:10]
    return '(' + first + ')' + ' ' + second + '-' + third


register.filter('phone_conversion', phone_conversion)

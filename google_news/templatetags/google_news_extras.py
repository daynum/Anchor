

from django import template
from django.template.defaulttags import register
register = template.Library()

@register.filter(name="key_to_string")
def key_to_string(dictionary, key):
    print("HOLAA")
    print(dictionary)
    return dictionary.get(key)
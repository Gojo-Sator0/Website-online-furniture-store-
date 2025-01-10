from django import template

from carts.utils import get_users_carts
from carts.models import Cart

register = template.Library()

@register.simple_tag()
def user_carts(request):
    return get_users_carts(request)
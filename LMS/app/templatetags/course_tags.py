from django import template
import math
from ..models import *
register = template.Library()


@register.simple_tag
def discount_calculation(price, discount):
    if discount is None or discount is 0:
        return price
    sellprice = price
    sellprice = price - (price * discount/100)
    return math.floor(sellprice)


@register.simple_tag
def speed_cal(number):
    number_count = int(number)
    print(number_count)

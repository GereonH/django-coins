from django import template
from django.template.defaultfilters import stringfilter
import requests
import json

register = template.Library()

@register.filter
@stringfilter
def get_json_by_id(coin_id, arg):
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/'+coin_id+'/')
    return(r.json()[0][arg])

@register.filter
@stringfilter
def get_png_by_id(coin_id, arg):
    img_url = 'https://files.coinmarketcap.com/static/img/coins/'+arg+'/'+coin_id+'.png'
    return img_url

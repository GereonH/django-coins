from django import template
import requests
import json

register = template.Library()

@register.filter(name='get_json_by_id')
def get_json_by_id(coin_id, arg):
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/'+coin_id+'/')
    return(r.json()[0][arg])

@register.filter(name='get_png_by_id')
def get_png_by_id(coin_id, arg):
    img_url = 'https://files.coinmarketcap.com/static/img/coins/'+arg+'/'+coin_id+'.png'
    return img_url

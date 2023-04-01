from django import template

register = template.Library()

@register.filter(name='cryptoname')
def cryptoname(cryptos, name):
    for crypto in cryptos:
        if crypto.name == name:
            return crypto

@register.filter(name='pricediff')
def pricediff(crypto):
    return (crypto.price - crypto.history_price)/100

from django.shortcuts import render
from django.http import HttpResponse

from .models import Crypto, TradeRecord

import random
from decimal import Decimal

def index(request):
    cryptos = Crypto.objects.all()
    context = {'cryptos': cryptos}
    return render(request, 'home/index.html', context)

def trade(request, cryptoname):
    try:
       crypto = Crypto.objects.get(name=cryptoname)
       trade_record = TradeRecord(crypto_name=crypto.name, crypto_price=crypto.price)
       trade_record.save()
       return HttpResponse('Trade succeeded')
    except:
       return HttpResponse('Trade failed')

def price_change(request, cryptoname):
    try:
       crypto = Crypto.objects.get(name=cryptoname)
       crypto.price = crypto.price + Decimal(random.uniform(-100,100))
       crypto.save()
       return HttpResponse('Price change succeeded')
    except:
       return HttpResponse('Price change failed')

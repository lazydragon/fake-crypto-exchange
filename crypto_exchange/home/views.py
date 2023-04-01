from django.shortcuts import render

from .models import Crypto


def index(request):
    cryptos = Crypto.objects.all()
    context = {'cryptos': cryptos}
    return render(request, 'home/index.html', context)

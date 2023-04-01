from django.shortcuts import render

from .models import Crypto


def index(request):
    context = {'cryptos': 1}
    return render(request, 'home/index.html', context)

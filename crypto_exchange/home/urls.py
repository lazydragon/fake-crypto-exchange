from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trade/<str:cryptoname>', views.trade, name='trade'),
    path('pricechange/<str:cryptoname>', views.price_change, name='price_change'),
]

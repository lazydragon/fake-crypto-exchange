from django.contrib import admin

from .models import Crypto, TradeRecord

class CryptoAdmin(admin.ModelAdmin):
    list_display = ('name','price')

class TradeRecordAdmin(admin.ModelAdmin):
    list_display = ('timestamp','crypto_name','crypto_price')
    ordering = ('-timestamp',)

# Register your models here.
admin.site.register(Crypto, CryptoAdmin)
admin.site.register(TradeRecord, TradeRecordAdmin)

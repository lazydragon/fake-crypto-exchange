from django.db import models

# Create your models here.
class Crypto(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    history_price = models.DecimalField(max_digits=10, decimal_places=2)
    

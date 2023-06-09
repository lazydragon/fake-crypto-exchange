# Generated by Django 4.1.7 on 2023-04-01 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('crypto_name', models.CharField(max_length=200)),
                ('crypto_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]

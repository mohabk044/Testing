# Generated by Django 4.2.2 on 2023-10-13 18:58

import creditcards.models
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_payment_shipment_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=creditcards.models.CardNumberField(max_length=25, validators=[django.core.validators.RegexValidator(message='Enter a valid card number (e.g., 1111 2222 3333 4444)', regex='^\\d{4} \\d{4} \\d{4} \\d{4}$')]),
        ),
    ]
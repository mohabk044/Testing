# Generated by Django 4.2.2 on 2023-10-13 19:06

import creditcards.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_alter_payment_card_number_alter_payment_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='expire',
            field=creditcards.models.CardExpiryField(help_text="Please enter the expiration date in the format 'mm/YY'."),
        ),
    ]
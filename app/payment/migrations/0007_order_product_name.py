# Generated by Django 3.2.4 on 2021-08-19 00:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('payment', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]

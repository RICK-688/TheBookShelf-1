# Generated by Django 3.2.4 on 2021-08-12 21:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('bookitem', '0005_auto_20210810_0146'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]

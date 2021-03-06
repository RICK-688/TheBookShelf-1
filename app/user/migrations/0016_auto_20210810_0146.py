# Generated by Django 3.2.4 on 2021-08-10 00:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0015_auto_20210810_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True,
                                                   choices=[(3, 'Editor'), (4, 'Admin'), (1, 'Reader'), (2, 'Author')],
                                                   default=1, null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('1d2bb223-cca9-4685-9b29-5741a2b57fb3'), editable=False,
                                   unique=True, verbose_name='Public identifier'),
        ),
    ]

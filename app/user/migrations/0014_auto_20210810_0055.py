# Generated by Django 3.2.4 on 2021-08-09 23:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0013_auto_20210810_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True,
                                                   choices=[(3, 'Editor'), (1, 'Reader'), (4, 'Admin'), (2, 'Author')],
                                                   default=1, null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='authuser',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('184f0fa0-0104-44fd-961d-3442a844777c'), editable=False,
                                   unique=True, verbose_name='Public identifier'),
        ),
    ]

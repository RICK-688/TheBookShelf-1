# Generated by Django 3.2.4 on 2021-06-26 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='plan', to='product.subscription_plan'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='topup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='topup', to='product.top_up_item'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='vip_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vip_account', to='product.user_profile'),
        ),
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='payment.billing_address'),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-26 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription_Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('is_featured', models.BooleanField(default=False)),
                ('num_available', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
        migrations.CreateModel(
            name='Top_up_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('book_coin', models.IntegerField(default=0)),
                ('monthly_ticket_number', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('num_available', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Balance', models.IntegerField(default=0)),
                ('plan_status', models.CharField(choices=[('VIP', 'VIP'), ('normal', 'Normal')], default='normal', max_length=20)),
                ('plan_end_date', models.DateTimeField(blank=True, null=True)),
                ('stripe_customer_id', models.CharField(blank=True, max_length=255, null=True)),
                ('stripe_subscription_id', models.CharField(blank=True, max_length=255, null=True)),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vip_status', to='product.subscription_plan')),
            ],
        ),
    ]

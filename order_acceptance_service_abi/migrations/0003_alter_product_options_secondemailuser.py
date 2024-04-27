# Generated by Django 5.0.4 on 2024-04-20 09:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_acceptance_service_abi', '0002_alter_product_gross_weight_of_box_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'номенклатуру', 'verbose_name_plural': 'Список СКЮ'},
        ),
        migrations.CreateModel(
            name='SecondEmailUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_email', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_unit_code', models.CharField(max_length=10, verbose_name='Код единицы продаж')),
                ('product_code', models.CharField(max_length=10, verbose_name='Код продукта')),
                ('option_number', models.PositiveIntegerField(verbose_name='Номер варианта')),
                ('barcode', models.PositiveIntegerField(verbose_name='Штрих-код')),
                ('net_weight_piece', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Вес нетто штуки, кг')),
                ('number_pieces_in_box', models.PositiveSmallIntegerField(verbose_name='Кол-во штук в коробе, шт')),
                ('net_weight_of_box', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Вес нетто короба, кг')),
                ('gross_weight_of_box', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Вес брутто короба, кг')),
                ('number_of_boxes_per_pallet', models.PositiveSmallIntegerField(verbose_name='Кол-во кор. на паллте, шт')),
                ('boxes_in_layer', models.PositiveSmallIntegerField(verbose_name='Коробок в слое')),
                ('factory', models.CharField(max_length=10, verbose_name='Завод')),
                ('expiration_date', models.PositiveSmallIntegerField(verbose_name='Срок годности, сут.')),
                ('product_name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('units_measurement', models.CharField(max_length=5, verbose_name='Ед. изм.')),
                ('brand_name', models.CharField(max_length=255, verbose_name='Бренд')),
                ('category', models.CharField(max_length=255, verbose_name='Категория')),
                ('product_group', models.CharField(max_length=255, verbose_name='Группа товара')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_active', models.BooleanField(default=True, verbose_name='Доступна к заказу')),
            ],
        ),
    ]

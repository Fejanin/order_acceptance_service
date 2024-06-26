from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    sales_unit_code = models.CharField(max_length=10, verbose_name="Код единицы продаж")
    product_code = models.CharField(max_length=10, verbose_name="Код продукта")
    option_number = models.PositiveIntegerField(verbose_name="Номер варианта")
    barcode = models.PositiveIntegerField(verbose_name="Штрих-код")
    net_weight_piece = models.DecimalField(decimal_places=3, max_digits=5, verbose_name="Вес нетто штуки, кг")
    number_pieces_in_box = models.PositiveSmallIntegerField(verbose_name="Кол-во штук в коробе, шт")
    net_weight_of_box = models.DecimalField(decimal_places=3, max_digits=5, verbose_name="Вес нетто короба, кг")
    gross_weight_of_box = models.DecimalField(decimal_places=3, max_digits=6, verbose_name="Вес брутто короба, кг")
    number_of_boxes_per_pallet = models.PositiveSmallIntegerField(verbose_name="Кол-во кор. на паллте, шт")
    boxes_in_layer = models.PositiveSmallIntegerField(verbose_name="Коробок в слое")
    factory = models.CharField(max_length=10, verbose_name="Завод")
    expiration_date = models.PositiveSmallIntegerField(verbose_name="Срок годности, сут.")
    product_name = models.CharField(max_length=255, verbose_name="Наименование")
    units_measurement = models.CharField(max_length=5, verbose_name="Ед. изм.")
    brand_name = models.CharField(max_length=255, verbose_name="Бренд")
    category = models.CharField(max_length=255, verbose_name="Категория")
    product_group = models.CharField(max_length=255, verbose_name="Группа товара")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_active = models.BooleanField(default=True, verbose_name="Доступна к заказу")

    class Meta:
        verbose_name = 'номенклатуру'
        verbose_name_plural = 'Список СКЮ'

    def __str__(self):
        return self.product_name


class SecondEmailUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='second_email')
    second_email = models.EmailField()

    def __str__(self):
        return self.second_email


class Order(models.Model):
    STATUSES_CHOICES = [
        ('SEND', 'ОТПРАВЛЕН'),
        ('TAKE', 'ПРИНЯТ В РАБОТУ'),
        ('CHAN', 'ОТМЕНЕН'),
        ('COMP', 'ВЫПОЛНЕН'),
    ]
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    product = models.ManyToManyField(Product, through='OrderProduct')
    status = models.CharField(max_length=4, choices=STATUSES_CHOICES, default='SEND', verbose_name="Статус")

    class Meta:
        ordering = ['-time_create']

    def __str__(self):
        return f'{self.time_create}#{self.pk}'

    def get_status(self):
        self.status_to_str = dict(self.STATUSES_CHOICES)[self.status]


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    count_product = models.DecimalField(decimal_places=2, max_digits=8, verbose_name="Количество")
    price = models.DecimalField(decimal_places=2, max_digits=8, default=0, verbose_name="Цена")

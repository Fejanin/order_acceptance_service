from django.contrib import admin
from .models import Product, SecondEmailUser, Order, OrderProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product_name',
        'sales_unit_code',
        'product_code',
        'option_number',
        'barcode',
        'factory',
        'expiration_date',
        'brand_name',
        'is_active',
    )
    list_display_links = ('product_name',)
    ordering = ('brand_name',)
    list_editable = ('is_active',)
    list_per_page = 15


@admin.register(SecondEmailUser)
class SecondEmailUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'second_email',
    )

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Заказы оптовых клиентов"
admin.site.register(Order)
admin.site.register(OrderProduct)

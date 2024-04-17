from django.contrib import admin
from .models import Product


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


# admin.site.register(Product, ProductAdmin)
admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Заказы оптовых клиентов"


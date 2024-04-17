from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render
from order_acceptance_service_abi.models import Product
from .utils import products_by_cat_dict, products_table_lst


@login_required
def start_page(request):
    data = {
        'title': 'Стартовая страница'}
    return render(request, 'order_acceptance_service_abi/start_page.html', data)


@login_required
def order(request):
    if request.method == 'POST':
        user_order = {'username': request.user.username}
        if request.user.is_authenticated:
            for i in request.POST:
                if 'id_' in i:
                    if request.POST[i]:
                        # request.POST[i] ==> str
                        try:
                            user_order[i] = round(float(request.POST[i]), 2)
                        except:
                            pass
        print(user_order)
    products = Product.objects.filter(is_active=True)
    products_by_cat = products_by_cat_dict(products)
    result = products_table_lst(products_by_cat)
    data = {
        'title': 'Заказ продукции',
        'products_by_cat': result,
    }
    return render(request, 'order_acceptance_service_abi/order.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

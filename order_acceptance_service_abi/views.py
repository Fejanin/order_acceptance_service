from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import render
from order_acceptance_service_abi.models import Product, Order, OrderProduct
from .utils import products_by_cat_dict, products_table_lst


@login_required
def start_page(request):
    orders = Order.objects.filter(user_id=request.user.id)
    data = {
        'title': 'Стартовая страница',
        'path': request.path,
        'orders': orders,
    }
    return render(request, 'order_acceptance_service_abi/start_page.html', data)


@login_required
def order(request):
    if request.method == 'POST':
        user = request.user
        user_order = {'username': user.username}
        if request.user.is_authenticated:
            # создать ф-цию в utils.py
            for i in request.POST:
                if 'product_id_' in i:
                    if request.POST[i]:
                        try:
                            user_order[i] = round(float(request.POST[i]), 2)
                        except:
                            pass
            if len(user_order) > 1:
                # создать ф-цию в utils.py
                new_order = Order(user=user)
                new_order.save()
                for i in user_order:
                    if i != 'username':
                        product_id = int(i.replace('product_id_', ''))
                        product_to_order = OrderProduct(
                            product=Product.objects.get(pk=product_id),
                            order=new_order,
                            count_product=user_order[i],
                        )
                        product_to_order.save()
    products = Product.objects.filter(is_active=True)
    products_by_cat = products_by_cat_dict(products)
    result = products_table_lst(products_by_cat)
    data = {
        'title': 'Заказ продукции',
        'products_by_cat': result,
        'path': request.path,
    }
    return render(request, 'order_acceptance_service_abi/order.html', data)


@login_required
def show_order(request, order_id):
    no_access = 'У вас нет доступа к данной странице!'
    user_pk = request.user.pk
    user_order = Order.objects.get(pk=order_id)
    if user_pk != user_order.user_id:
        data = {
            'title': no_access,
            'no_access': no_access,
        }
    else:
        products = OrderProduct.objects.filter(order_id=order_id)
        data = {
            'title': f'Заказ N{order_id} от пользователя {User.objects.get(pk=user_order.user_id)}',
            'products': products,
            'no_access': no_access,
        }
    return render(request, 'order_acceptance_service_abi/show_order.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

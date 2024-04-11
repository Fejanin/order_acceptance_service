from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


@login_required
def start_page(request):
    data = {'title': 'Стартовая страница'}
    return render(request, 'order_acceptance_service_abi/start_page.html', data)


@login_required
def order(request):
    data = {'title': 'Заказ продукции'}
    return render(request, 'order_acceptance_service_abi/order.html', data)

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    data = {'title': 'Заказ продукции'}
    return render(request, 'order_acceptance_service_abi/index.html', data)

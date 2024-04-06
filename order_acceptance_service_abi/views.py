from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'order_acceptance_service_abi/index.html')

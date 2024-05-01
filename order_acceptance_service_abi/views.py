from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseNotFound , FileResponse
from django.shortcuts import render
from order_acceptance_service_abi.models import Product, Order, OrderProduct
from .forms import UploadFileForm
from .utils import products_by_cat_dict, products_table_lst, upgrade_products_table, handle_uploaded_file
import os


@login_required
def start_page(request):
    data = {
        'title': 'Стартовая страница',
        'path': request.path,
    }
    user = request.user
    if user.is_superuser:
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(user_id=request.user.id)
    data['orders'] = orders
    return render(request, 'order_acceptance_service_abi/start_page.html', data)


@login_required
def order(request):
    if request.method == 'POST':
        user = request.user
        user_order = {'username': user.username}
        for i in request.POST:
            if 'product_id_' in i:
                if request.POST[i]:
                    try:
                        user_order[i] = round(float(request.POST[i]), 2)
                    except:
                        pass
        if len(user_order) > 1:
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
    data = {
        'title': no_access,
        'no_access': no_access,
    }
    user_pk = request.user.pk
    user_order = Order.objects.get(pk=order_id)
    if request.user.is_superuser:
        products = OrderProduct.objects.filter(order_id=order_id)
        data['products'] = products
        data['title'] = Order.objects.get(pk=order_id)
        if request.method == 'POST':
            return download(products, order_id, user_order)
    elif user_pk == user_order.user_id:
        products = OrderProduct.objects.filter(order_id=order_id)
        data['products'] = products
        data['title'] = Order.objects.get(pk=order_id)
    return render(request, 'order_acceptance_service_abi/show_order.html', data)


def download(products, order_id, user_order):
    directory = 'orders'
    files = os.listdir(directory)
    for f in files:
        os.remove(f'{directory}/{f}')
    filename = f'orders/{user_order.user.username} заказ №{order_id} {str(user_order.time_create)[:19].replace(":", ".")}.txt'
    with open(filename, 'w', encoding='UTF-8') as f:
        f.writelines(f'{user_order.time_create}\n')
        for p in products:
            f.writelines(f'{p.product.sales_unit_code}\t{p.product.product_code}\t{p.product.option_number}\t{p.product.barcode}\t{p.product.product_name}\t{p.count_product}\n')
    response = FileResponse(open(filename, 'rb'), as_attachment=True, filename=filename)
    return response


@login_required
def upload_file(request):
    directory = 'uploads'
    data = {
        'title': f'Загрузка файла',
    }
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
            files = os.listdir(directory)
            lst_products_new = upgrade_products_table(files[0])
            if lst_products_new:
                Product.objects.update(is_active=False)
                for i in lst_products_new:
                    obj = Product.objects.filter(
                        sales_unit_code=i['sales_unit_code'],
                        product_code=i['product_code'],
                        option_number=i['option_number'],
                        barcode=i['barcode'],
                        net_weight_piece=i['net_weight_piece'],
                        number_pieces_in_box=i['number_pieces_in_box'],
                        net_weight_of_box=i['net_weight_of_box'],
                        gross_weight_of_box=i['gross_weight_of_box'],
                        number_of_boxes_per_pallet=i['number_of_boxes_per_pallet'],
                        boxes_in_layer=i['boxes_in_layer'],
                        factory=i['factory'],
                        expiration_date=i['expiration_date'],
                        product_name=i['product_name'],
                        units_measurement=i['units_measurement'],
                        brand_name=i['brand_name'],
                        category=i['category'],
                        product_group=i['product_group'],
                    )
                    if obj:
                        current_product = obj[0]
                        current_product.is_active = True
                        current_product.save()
                    else:
                        try:
                            Product.objects.create(
                                sales_unit_code=i['sales_unit_code'],
                                product_code=i['product_code'],
                                option_number=i['option_number'],
                                barcode=i['barcode'],
                                net_weight_piece=i['net_weight_piece'],
                                number_pieces_in_box=i['number_pieces_in_box'],
                                net_weight_of_box=i['net_weight_of_box'],
                                gross_weight_of_box=i['gross_weight_of_box'],
                                number_of_boxes_per_pallet=i['number_of_boxes_per_pallet'],
                                boxes_in_layer=i['boxes_in_layer'],
                                factory=i['factory'],
                                expiration_date=i['expiration_date'],
                                product_name=i['product_name'],
                                units_measurement=i['units_measurement'],
                                brand_name=i['brand_name'],
                                category=i['category'],
                                product_group=i['product_group'],
                            )
                        except IntegrityError as e:
                            print(e)
                os.remove(f'{directory}/{files[0]}')
    else:
        form = UploadFileForm()
    data['form'] = form
    files = os.listdir(directory)
    if files:
        data['files'] = files
    return render(request, 'order_acceptance_service_abi/upload_file.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

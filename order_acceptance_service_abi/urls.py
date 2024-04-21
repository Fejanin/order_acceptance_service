from django.urls import path
from . import views
from .views import page_not_found


urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('<int:order_id>', views.show_order, name='show_order'),
    path('order/', views.order, name='order'),
]

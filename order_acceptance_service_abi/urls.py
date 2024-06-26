from django.urls import path
from . import views


urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('<int:order_id>', views.show_order, name='show_order'),
    path('order/', views.order, name='order'),
    path('upload/', views.upload_file, name='upload_file'),
]

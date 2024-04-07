from django.urls import path
from . import views


# создаем переменную, именнующую пространство имен
app_name = "users"

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]

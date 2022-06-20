from django.urls import path
from rest_framework.authtoken import views as v
from . import views

urlpatterns = [
    path('api/login', views.CustomAuthToken.as_view() , name="login"),
    path('api/register', views.register_user , name="register"),


    path('api/create_order', views.create_order , name="create-order"),
    path('api/add_orderItems', views.adding_orderItem , name="add-orderItems"),


    path('api/products', views.products_list , name="product-list"),
    path('api/orders', views.orders_list , name="orders-list"),
    path('api/orders/logged-in-user/', views.user_orders,name='logged-in-user'),

    
]
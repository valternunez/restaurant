from django.urls import path

from . import views 


urlpatterns = [
    path('', views.order_list, name = 'orders'),
    path('<int:id>', views.order_detail, name = 'order_detail'),
    path('orders', views.client_order_list, name = 'client_order_list'),
    path('detail/<int:id>', views.client_order_detail, name = 'client_order_detail'),
]
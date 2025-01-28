from django.urls import path
from order.views import OrderListView, OrderCreateView, OrderDeleteView


app_name = 'orders'

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('make_order/', OrderCreateView.as_view(), name='order-create'),
    path('order_delete/<int:pk>/', OrderDeleteView.as_view(), name='order-delete'),
]

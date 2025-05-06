# orders/urls.py
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('cart/',          views.CartView.as_view(),        name='cart'),
    path('add/<int:service_id>/',    views.AddItemView.as_view(),    name='add_item'),
    path('update/<int:item_id>/',    views.UpdateItemView.as_view(), name='update_item'),
    path('remove/<int:item_id>/',    views.RemoveItemView.as_view(), name='remove_item'),
    path('checkout/',      views.CheckoutView.as_view(),    name='checkout'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='detail'),
]

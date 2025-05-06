# orders/views.py
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, View, DetailView
from services.models import Service
from .models import Order, OrderItem
from .forms import CheckoutForm

class CartView(TemplateView):
    template_name = 'orders/cart.html'
    def get_context_data(self, **ctx):
        ctx = super().get_context_data(**ctx)
        ctx['cart'] = Order.objects.get_or_create(user=self.request.user, estado='pending')[0]
        return ctx

class AddItemView(View):
    def post(self, request, service_id):
        order, _ = Order.objects.get_or_create(user=request.user, estado='pending')
        svc = get_object_or_404(Service, id=service_id)
        cantidad = int(request.POST.get('cantidad', 1))
        item, created = OrderItem.objects.get_or_create(
            order=order, service=svc,
            defaults={'cantidad':cantidad, 'precio_unitario': svc.precio}
        )
        if not created:
            item.cantidad = cantidad
            item.save()
        return redirect('orders:cart')

class UpdateItemView(View):
    def post(self, request, item_id):
        item = get_object_or_404(OrderItem, id=item_id, order__user=request.user)
        item.cantidad = int(request.POST.get('cantidad', item.cantidad))
        item.save()
        return redirect('orders:cart')

class RemoveItemView(View):
    def post(self, request, item_id):
        item = get_object_or_404(OrderItem, id=item_id, order__user=request.user)
        item.delete()
        return redirect('orders:cart')

class CheckoutView(TemplateView):
    template_name = 'orders/checkout.html'
    def get_context_data(self, **ctx):
        ctx = super().get_context_data(**ctx)
        ctx['cart'] = Order.objects.get(user=self.request.user, estado='pending')
        ctx['form'] = CheckoutForm()
        return ctx
    def post(self, request):
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.get(user=request.user, estado='pending')
            order.estado = 'paid'
            order.save()
            return redirect('orders:detail', pk=order.id)
        return self.get(request)

class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'

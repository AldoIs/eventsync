from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('precio_unitario',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'fecha_creacion', 'estado')
    list_filter = ('estado', 'fecha_creacion')
    inlines = [OrderItemInline]
    search_fields = ('user__username', 'id')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'service', 'cantidad', 'precio_unitario')
    search_fields = ('service__nombre',)

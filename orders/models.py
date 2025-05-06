from django.conf import settings
from django.db import models
from services.models import Service

class Order(models.Model):
    ESTADOS = [
        ('pending', 'Pendiente'),
        ('paid', 'Pagado'),
        ('completed', 'Completado'),
        ('cancelled', 'Cancelado'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pending')
    @property
    def total_price(self):
        """
        Retorna el total de todos los items: sum(precio_unitario * cantidad).
        """
        return sum(item.precio_unitario * item.cantidad for item in self.items.all())

    def __str__(self):
        return f'Order #{self.id} ({self.get_estado_display()})'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        unique_together = ('order', 'service')

    def __str__(self):
        return f'{self.cantidad}× {self.service.nombre}'

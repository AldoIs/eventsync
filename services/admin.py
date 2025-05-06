from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'created_at')
    search_fields = ('nombre',)
    list_filter = ('created_at',)

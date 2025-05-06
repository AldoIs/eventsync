from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Agrega el campo teléfono al formulario de admin
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('telefono',)}),
    )
    list_display = ('username', 'email', 'telefono', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'telefono')

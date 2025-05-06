# orders/forms.py

from django import forms

class CheckoutForm(forms.Form):
    nombre = forms.CharField(
        label='Nombre completo',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    direccion = forms.CharField(
        label='Dirección',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2})
    )
    tarjeta_numero = forms.CharField(
        label='Número de tarjeta',
        max_length=19,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '•••• •••• •••• ••••'})
    )
    tarjeta_expiracion = forms.CharField(
        label='Expiry (MM/AA)',
        max_length=5,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/AA'})
    )
    tarjeta_cvv = forms.CharField(
        label='CVV',
        max_length=4,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '•••'})
    )

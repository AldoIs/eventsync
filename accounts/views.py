# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User
from .forms import RegisterForm

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

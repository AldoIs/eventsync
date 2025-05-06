from django.views.generic import ListView, DetailView
from .models import Service

class HomeView(ListView):
    model = Service
    template_name = 'home.html'
    context_object_name = 'services'
    paginate_by = 12

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
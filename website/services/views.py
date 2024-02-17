from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)
from django.contrib import messages
from .forms import ServiceForm
from .models import Service
# Create your views here.



class ServiceListView(ListView):
    model = Service
    template_name = 'services/services_list.html'
    context_object_name = 'services'

    def get(self, request):
        # Check for success messages and pass them to the template
        success_messages = messages.get_messages(request)
        success_messages_list = [message.message for message in success_messages if message.level == messages.SUCCESS]
        services = Service.objects.all()

        return render(request, self.template_name, {'services': services, 'success_messages': success_messages_list})
    
class CreateServiceView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name= "services/services_form.html"
    success_url = reverse_lazy('service_list')
    def form_valid(self, form):
        messages.success(self.request, 'service added successfully.')
        return super().form_valid(form)


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'services'
    template_name = 'services/services_detail.html'
    def get(self, request, pk):
        services = get_object_or_404(Service, pk=pk)

        # Check for success messages and pass them to the template
        success_messages = messages.get_messages(request)
        success_messages_list = [message.message for message in success_messages if message.level == messages.SUCCESS]

        return render(request, self.template_name, {'services': services, 'success_messages': success_messages_list})
    
class EditServiceView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name= "services/services_form.html"
    success_url = reverse_lazy('service_list')
    def form_valid(self, form):
        messages.success(self.request, 'service updated successfully.')
        return super().form_valid(form)
    
class DeleteServiceView(DeleteView):
    model = Service
    template_name= "services/services_confirm_delete.html"
    success_url = reverse_lazy('service_list')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'service has been deleted successfully.')
        return super().delete(request, *args, **kwargs)
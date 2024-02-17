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
from .forms import TechnologyForm
from .models import Technology
# Create your views here.



class TechnologyListView(ListView):
    model = Technology
    template_name = 'technologies/technologies_list.html'
    context_object_name = 'technologys'

    def get(self, request):
        # Check for success messages and pass them to the template
        success_messages = messages.get_messages(request)
        success_messages_list = [message.message for message in success_messages if message.level == messages.SUCCESS]
        technologys = Technology.objects.all()

        return render(request, self.template_name, {'technologys': technologys, 'success_messages': success_messages_list})
    
class CreateTechnologyView(CreateView):
    model = Technology
    form_class = TechnologyForm
    template_name= "technologies/technologies_form.html"
    success_url = reverse_lazy('technology_list')
    def form_valid(self, form):
        messages.success(self.request, 'technology added successfully.')
        return super().form_valid(form)


class TechnologyDetailView(DetailView):
    model = Technology
    context_object_name = 'technologys'
    template_name = 'technologies/technologies_detail.html'
    def get(self, request, pk):
        technologys = get_object_or_404(Technology, pk=pk)

        # Check for success messages and pass them to the template
        success_messages = messages.get_messages(request)
        success_messages_list = [message.message for message in success_messages if message.level == messages.SUCCESS]

        return render(request, self.template_name, {'technologys': technologys, 'success_messages': success_messages_list})
    
class EditTechnologyView(UpdateView):
    model = Technology
    form_class = TechnologyForm
    template_name= "technologies/technologies_form.html"
    success_url = reverse_lazy('technology_list')
    def form_valid(self, form):
        messages.success(self.request, 'technology updated successfully.')
        return super().form_valid(form)
    
class DeleteTechnologyView(DeleteView):
    model = Technology
    success_url = reverse_lazy('technology_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'technology has been deleted successfully.')
        return super().delete(request, *args, **kwargs)
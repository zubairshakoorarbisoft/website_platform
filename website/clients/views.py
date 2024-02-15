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
from .forms import TestimonialForm
from .models import Testimonial
# Create your views here.



class TestimonialListView(ListView):
    model = Testimonial
    template_name = 'clients/testimonial_list.html'
    context_object_name = 'clients'

    def get(self, request):
        # Check for success messages and pass them to the template
        success_messages = messages.get_messages(request)
        success_messages_list = [message.message for message in success_messages if message.level == messages.SUCCESS]
        testimonials = Testimonial.objects.all()

        return render(request, self.template_name, {'testimonials': testimonials, 'success_messages': success_messages_list})
    
class CreateTestimonialView(CreateView):
    model = Testimonial
    form_class = TestimonialForm
    def form_valid(self, form):
        messages.success(self.request, 'Testimonial added successfully.')
        return super().form_valid(form)


class TestimonialDetailView(DetailView):
    model = Testimonial
    context_object_name = 'testimonials'
    template_name = 'clients/testimonial_detail.html'

    def get(self, request, pk):
        testimonials = get_object_or_404(Testimonial, pk=pk)

        # Check for success messages and pass them to the template
        success_messages = messages.get_messages(request)
        success_messages_list = [message.message for message in success_messages if message.level == messages.SUCCESS]

        return render(request, self.template_name, {'testimonials': testimonials, 'success_messages': success_messages_list})
    
class EditTestimonialView(UpdateView):
    model = Testimonial
    form_class = TestimonialForm
    success_url = reverse_lazy('testimonial_list')
    def form_valid(self, form):
        messages.success(self.request, 'Testimonial updated successfully.')
        return super().form_valid(form)
    
class DeleteTestimonialView(DeleteView):
    model = Testimonial
    success_url = reverse_lazy('testimonial_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Testimonial has been deleted successfully.')
        return super().delete(request, *args, **kwargs)
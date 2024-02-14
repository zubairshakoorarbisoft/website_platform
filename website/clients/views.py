from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)
from django.contrib import messages
# from .forms import JobForm
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

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)
from django.contrib import messages
from .forms import JobForm
from .models import Job


class CreateJobView(CreateView):
    model = Job
    form_class = JobForm

    def form_valid(self, form):
        messages.success(self.request, 'Job added successfully.')
        return super().form_valid(form)


class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'jobs/job_detail.html'

    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk)

        # Check for success messages and pass them to the template
        success_messages = messages.get_messages(request)
        success_messages_list = [message.message for message in success_messages if message.level == messages.SUCCESS]

        return render(request, self.template_name, {'job': job, 'success_messages': success_messages_list})

class EditJobView(UpdateView):
    model = Job
    form_class = JobForm

    def form_valid(self, form):
        messages.success(self.request, 'Job updated successfully.')
        return super().form_valid(form)


class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'


    def get(self, request):
        # Check for success messages and pass them to the template
        success_messages = messages.get_messages(request)
        success_messages_list = [message.message for message in success_messages if message.level == messages.SUCCESS]
        jobs = Job.objects.all()

        return render(request, self.template_name, {'jobs': jobs, 'success_messages': success_messages_list})


class DeleteJobView(DeleteView):
    model = Job
    success_url = reverse_lazy('job_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Job deleted successfully.')
        return super().delete(request, *args, **kwargs)
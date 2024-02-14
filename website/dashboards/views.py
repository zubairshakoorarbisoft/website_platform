from django.views.generic import TemplateView

from jobs.models import Job
from clients.models import Client

class DashboardsView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context data if needed
        context['total_jobs'] = Job.objects.count()
        context['testimonial_list'] = Client.objects.count()
        return context
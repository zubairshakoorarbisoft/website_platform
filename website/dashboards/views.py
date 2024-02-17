from django.views.generic import TemplateView

from jobs.models import Job
from clients.models import Client
from products.models import Product
from services.models import Service
from technologies.models import Technology

class DashboardsView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context data if needed
        context['total_jobs'] = Job.objects.count()
        context['total_testimonial'] = Client.objects.count()
        context['total_product'] = Product.objects.count()
        context['total_service'] = Service.objects.count()
        context['total_technology'] = Technology.objects.count()
        return context
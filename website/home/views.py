from django.conf import settings
from django.views.generic import TemplateView, DetailView
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from clients.models import ClientQuery, Testimonial
from jobs.models import Job
from services.models import Service
from products.models import Product
from technologies.models import Technology


class HomePageView(TemplateView):
    template_name= 'home/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the testimonials and pass them to the context
        testimonials = Testimonial.objects.all()
        all_services = Service.objects.all()
        all_products= Product.objects.all()
        context["testimonials"] = testimonials
        context["all_services"] = all_services
        context["all_products"] = all_products
        context["MEDIA_URL"] = settings.MEDIA_URL
        return context 

class CareersPageView(TemplateView):
    template_name = "home/job_listing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["open_jobs"] = Job.objects.all()
        return context
    
class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job_detail'
    template_name = 'home/single_job.html'

    def get(self, request, pk):
        job_detail = get_object_or_404(Job, pk=pk)
        return render(request, self.template_name, {'job_detail': job_detail})

   
class SingleServicePage(DetailView):
    model = Service
    context_object_name = 'service_detail'
    template_name = "home/single_service.html"

    def get(self, request, pk):
        service_detail = get_object_or_404(Service, pk=pk)
        return render(request, self.template_name, {'service_detail': service_detail})


  
class SingleProductPage(DetailView):
    model = Product
    context_object_name = 'product_detail'
    template_name = "home/single_product.html"

    def get(self, request, pk):
        product_detail = get_object_or_404(Product, pk=pk)
        return render(request, self.template_name, {'product_detail': product_detail})


  
class SingleTechnologyPage(DetailView):
    model = Technology
    context_object_name = 'technology_detail'
    template_name = "home/single_technology.html"

    def get(self, request, pk):
        technology_detail = get_object_or_404(Technology, pk=pk)
        return render(request, self.template_name, {'technology_detail': technology_detail})





@require_POST
def submit_contact_us_form(request):
    service = request.POST.get('service')
    org_name = request.POST.get('org_name')
    email = request.POST.get('email')
    full_name = request.POST.get('full_name')
    requirements = request.POST.get('requirements')

    # If there are validation errors, return a JSON response with errors
    if not all([service, org_name, email, full_name, requirements]):
        errors = {'error': 'All fields are required.'}
        return JsonResponse(errors, status=400)

    ClientQuery(
        service_name=service,
        company_name=org_name,
        email=email,
        full_name=full_name,
        requirements=requirements
    ).save()

    # Return a success response
    return JsonResponse({'success': True})


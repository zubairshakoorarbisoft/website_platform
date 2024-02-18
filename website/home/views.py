from django.conf import settings
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render
from clients.models import ClientQuery, Testimonial
from jobs.models import Job
from services.models import Service
from products.models import Product



class HomePageView(TemplateView):
    template_name = "home/index.html"

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

# Services listing through Functional views
def ServiceDetail(request):
    servicedetail= Service.objects.all()
    # servicedetail= Service.objects.get(url=url)
    my_dict_data= {
        'servicedetail': servicedetail,
    }
    # Render the view to multiple templates
    template_names = [
        'home/service_page.html'
        ]
    print(servicedetail)  
    return render(request, template_names , my_dict_data )

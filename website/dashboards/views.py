from django.views.generic import TemplateView
from django.shortcuts import render, redirect, HttpResponse
from jobs.models import Job
from clients.models import Client
from products.models import Product
from services.models import Service
from technologies.models import Technology

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def sign_in(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect()
        else:
            return HttpResponse(" <h3>Username or Password is incorrect! Try again </h3>")
    
    return render (request, 'dashboards/login.html')

   
def sign_out(request):
     logout(request)
     return redirect('sign-in')


class DashboardsView(TemplateView):
    template_name = 'dashboards/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add additional context data if needed
        context['total_jobs'] = Job.objects.count()
        context['total_testimonial'] = Client.objects.count()
        context['total_product'] = Product.objects.count()
        context['total_service'] = Service.objects.count()
        context['total_technology'] = Technology.objects.count()
        return context
    

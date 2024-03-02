from django.urls import path
from .views import(
     HomePageView, 
     CareersPageView, 
     submit_contact_us_form,
     SingleServicePage,
     SingleProductPage,
     SingleTechnologyPage,
     JobDetailView
)

from .import views


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact-us/', submit_contact_us_form, name='submit_contact_us_form'),
    path('service/',  SingleServicePage.as_view(), name='all_services' ),
    path('product/',  SingleProductPage.as_view(), name='all_products' ),
    path('technology/',  SingleTechnologyPage.as_view(), name='all_technologys' ),
    path('careers/', CareersPageView.as_view(), name='careers'),
    path('careers/<str:pk>/',  JobDetailView.as_view(), name='job_detail' ),



]
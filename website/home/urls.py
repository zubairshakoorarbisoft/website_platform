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
    path('service/<str:url>/',  SingleServicePage.as_view(), name='service_detail' ),
    path('product/<str:url>/',  SingleProductPage.as_view(), name='product_detail' ),
    path('technology/<str:url>/',  SingleTechnologyPage.as_view(), name='technology_detail' ),
    path('careers/', CareersPageView.as_view(), name='careers'),
    path('careers/<str:pk>/',  JobDetailView.as_view(), name='job_detail' ),



]
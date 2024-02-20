from django.urls import path
from .views import HomePageView, CareersPageView, submit_contact_us_form
from .import views


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('careers/', CareersPageView.as_view(), name='careers'),
    path('contact_us/', submit_contact_us_form, name='submit_contact_us_form'),
    # path('services/<slug:url>/',  views.ServiceDetail, name='services' )
]
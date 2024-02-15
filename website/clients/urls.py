from django.urls import path
from .views import(
    TestimonialListView,
    CreateTestimonialView,
    TestimonialDetailView,
    EditTestimonialView,
    DeleteTestimonialView
    
) 

urlpatterns = [
    path('', TestimonialListView.as_view(), name='testimonial_list'),
    path('create/', CreateTestimonialView.as_view(), name='create_testimonial'),
    path('detail/<int:pk>', TestimonialDetailView.as_view(), name='testimonial_detail'),
    path('edit/<int:pk>/', EditTestimonialView.as_view(), name='edit_testimonial'),
    path('delete/<int:pk>/', DeleteTestimonialView.as_view(), name='delete_testimonial'),
]






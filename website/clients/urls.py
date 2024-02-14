from django.urls import path
from .views import(
    TestimonialListView
    
) 

urlpatterns = [
    path('', TestimonialListView.as_view(), name='testimonial_list'),
    # path('create/', CreateJobView.as_view(), name='create_job'),
    # path('detail/<int:pk>', JobDetailView.as_view(), name='job_detail'),
    # path('edit/<int:pk>/', EditJobView.as_view(), name='edit_job'),
    # path('delete/<int:pk>/', DeleteJobView.as_view(), name='delete_job'),
]






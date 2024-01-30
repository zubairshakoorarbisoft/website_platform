from django.urls import path
from .views import (
    CreateJobView,
    DeleteJobView,
    EditJobView,
    JobDetailView,
    JobListView
)


urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('create/', CreateJobView.as_view(), name='create_job'),
    path('detail/<int:pk>', JobDetailView.as_view(), name='job_detail'),
    path('edit/<int:pk>/', EditJobView.as_view(), name='edit_job'),
    path('delete/<int:pk>/', DeleteJobView.as_view(), name='delete_job'),
]
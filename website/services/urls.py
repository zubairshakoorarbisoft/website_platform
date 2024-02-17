from django.urls import path
from .views import(
    ServiceListView,
    CreateServiceView,
    ServiceDetailView,
    EditServiceView,
    DeleteServiceView
    
) 

urlpatterns = [
    path('', ServiceListView.as_view(), name='service_list'),
    path('detail/<int:pk>', ServiceDetailView.as_view(), name='service_detail'),
    path('create/', CreateServiceView.as_view(), name='create_service'),
    path('edit/<int:pk>/', EditServiceView.as_view(), name='edit_service'),
    path('delete/<int:pk>/', DeleteServiceView.as_view(), name='delete_service'),
]






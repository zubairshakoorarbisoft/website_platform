from django.urls import path
from .views import(
    TechnologyListView,
    CreateTechnologyView,
    TechnologyDetailView,
    EditTechnologyView,
    DeleteTechnologyView
    
) 

urlpatterns = [
    path('', TechnologyListView.as_view(), name='technology_list'),
    path('detail/<int:pk>', TechnologyDetailView.as_view(), name='technology_detail'),
    path('create/', CreateTechnologyView.as_view(), name='create_technology'),
    path('edit/<int:pk>/', EditTechnologyView.as_view(), name='edit_technology'),
    path('delete/<int:pk>/', DeleteTechnologyView.as_view(), name='delete_technology'),
]






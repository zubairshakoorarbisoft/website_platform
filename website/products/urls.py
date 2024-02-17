from django.urls import path
from .views import(
    ProductListView,
    CreateProductView,
    ProductDetailView,
    EditProductView,
    DeleteProductView
    
) 

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('create/', CreateProductView.as_view(), name='create_product'),
    path('edit/<int:pk>/', EditProductView.as_view(), name='edit_product'),
    path('delete/<int:pk>/', DeleteProductView.as_view(), name='delete_product'),
]






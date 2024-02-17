from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)
from django.contrib import messages
from .forms import ProductForm
from .models import Product
# Create your views here.



class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get(self, request):
        # Check for success messages and pass them to the template
        success_messages = messages.get_messages(request)
        success_messages_list = [message.message for message in success_messages if message.level == messages.SUCCESS]
        products = Product.objects.all()

        return render(request, self.template_name, {'products': products, 'success_messages': success_messages_list})
    
class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    def form_valid(self, form):
        messages.success(self.request, 'Product added successfully.')
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/product_detail.html'

    def get(self, request, pk):
        products = get_object_or_404(Product, pk=pk)

        # Check for success messages and pass them to the template
        success_messages = messages.get_messages(request)
        success_messages_list = [message.message for message in success_messages if message.level == messages.SUCCESS]

        return render(request, self.template_name, {'products': products, 'success_messages': success_messages_list})
    
class EditProductView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    def form_valid(self, form):
        messages.success(self.request, 'Product updated successfully.')
        return super().form_valid(form)
    
class DeleteProductView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Product has been deleted successfully.')
        return super().delete(request, *args, **kwargs)
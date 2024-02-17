from django import forms
from django.core.validators import MinValueValidator

from datetime import datetime as dt

from .widgets import PRODUCT_FORM_WIDGET
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = PRODUCT_FORM_WIDGET
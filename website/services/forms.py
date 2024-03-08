from django import forms
from django.core.validators import MinValueValidator

from datetime import datetime as dt

from .widgets import SERVICES_FORM_WIDGET
from .models import Service , SubServices
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = SERVICES_FORM_WIDGET


class SubServiceForm(forms.ModelForm):
    class Meta:
        model = SubServices
        fields = '__all__'
        # widgets = SUB_SERVICES_FORM_WIDGET

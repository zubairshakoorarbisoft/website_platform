from django import forms
from django.core.validators import MinValueValidator

from datetime import datetime as dt

from .widgets import SERVICES_FORM_WIDGET
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = SERVICES_FORM_WIDGET
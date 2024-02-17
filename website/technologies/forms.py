from django import forms
from django.core.validators import MinValueValidator

from datetime import datetime as dt

from .widgets import TECHNOLOGY_FORM_WIDGET
from .models import Technology

class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = '__all__'
        widgets = TECHNOLOGY_FORM_WIDGET
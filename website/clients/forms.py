from django import forms
from django.core.validators import MinValueValidator

from datetime import datetime as dt

from .widgets import TESTIMONIAL_FORM_WIDGET
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'
        widgets = TESTIMONIAL_FORM_WIDGET
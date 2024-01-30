# forms.py
from django import forms
from django.core.validators import MinValueValidator

from datetime import datetime as dt

from .widgets import JOB_FORM_WIDGET
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        widgets = JOB_FORM_WIDGET

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set a custom error message for the no_of_positions field
        self.fields['no_of_positions'].validators.append(
            MinValueValidator(1, message="Ensure No of positions are greater than or equal to 1.")
        )
        self.fields['last_date_to_apply'].validators.append(
            MinValueValidator(dt.now().date(), message="Last date to apply cannot be older than today")
        )

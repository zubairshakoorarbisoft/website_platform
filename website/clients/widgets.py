from django import forms


TESTIMONIAL_FORM_WIDGET = {
    'company_name': forms.TextInput(attrs={'class': 'form-control'}),
    'giver_name': forms.TextInput(attrs={'class': 'form-control'}),
    'giver_designation': forms.TextInput(attrs={'class': 'form-control'}),
    'content': forms.Textarea(attrs={'class': 'form-control'}),
    'rating': forms.NumberInput(attrs={'class': 'form-control'}),
    }
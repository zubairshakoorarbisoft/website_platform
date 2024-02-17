from django import forms


SERVICES_FORM_WIDGET = {
    'service_name': forms.TextInput(attrs={'class': 'form-control'}),
    'service_discription': forms.TextInput(attrs={'class': 'form-control'}),
    'content': forms.Textarea(attrs={'class': 'form-control'})
    }
from django import forms


TECHNOLOGY_FORM_WIDGET = {
    'technology_name': forms.TextInput(attrs={'class': 'form-control'}),
    'technology_discription': forms.TextInput(attrs={'class': 'form-control'}),
    'content': forms.Textarea(attrs={'class': 'form-control'}),
    }
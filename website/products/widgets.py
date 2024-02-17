from django import forms


PRODUCT_FORM_WIDGET = {
    'product_name': forms.TextInput(attrs={'class': 'form-control'}),
    'product_discription': forms.TextInput(attrs={'class': 'form-control'}),
    'content': forms.Textarea(attrs={'class': 'form-control'}),
    }
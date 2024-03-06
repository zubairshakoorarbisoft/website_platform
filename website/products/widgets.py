from django import forms


PRODUCT_FORM_WIDGET = {
    'product_name': forms.TextInput(attrs={'class': 'form-control'}),
    'url': forms.TextInput(attrs={'class': 'form-control'}),
    'h1': forms.TextInput(attrs={'class': 'form-control'}),
    'product_discription': forms.TextInput(attrs={'class': 'form-control'}),
    'h2': forms.TextInput(attrs={'class': 'form-control'}),
    'content': forms.TextInput(attrs={'class': 'form-control'}),
    'process_1': forms.TextInput(attrs={'class': 'form-control'}),
    'process_1_disc': forms.TextInput(attrs={'class': 'form-control'}),
    'process_2': forms.TextInput(attrs={'class': 'form-control'}),
    'process_2_disc': forms.TextInput(attrs={'class': 'form-control'}),
    'process_3': forms.TextInput(attrs={'class': 'form-control'}),
    'process_3_disc': forms.TextInput(attrs={'class': 'form-control'}),
    'process_4': forms.TextInput(attrs={'class': 'form-control'}),
    'process_4_disc': forms.TextInput(attrs={'class': 'form-control'}),    
    'usage_1': forms.TextInput(attrs={'class': 'form-control'}),
    'usage_1_disc': forms.TextInput(attrs={'class': 'form-control'}),
    'usage_2': forms.TextInput(attrs={'class': 'form-control'}),
    'usage_2_disc': forms.TextInput(attrs={'class': 'form-control'}),
    'usage_3': forms.TextInput(attrs={'class': 'form-control'}),
    'usage_3_disc': forms.TextInput(attrs={'class': 'form-control'}),
    'usage_4': forms.TextInput(attrs={'class': 'form-control'}),
    'usage_4_disc': forms.TextInput(attrs={'class': 'form-control'}),
    
    }
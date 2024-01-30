from django import forms


JOB_FORM_WIDGET = {
    'display_title': forms.TextInput(attrs={'class': 'form-control'}),
    'no_of_positions': forms.NumberInput(attrs={'class': 'form-control'}),
    'job_description': forms.Textarea(attrs={'class': 'form-control'}),
    'location': forms.TextInput(attrs={'class': 'form-control'}),
    'last_date_to_apply': forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }),
    'domain': forms.TextInput(attrs={'class': 'form-control'}),
}
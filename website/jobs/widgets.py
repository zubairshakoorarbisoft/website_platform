from django import forms


JOB_FORM_WIDGET = {
    'display_title': forms.TextInput(attrs={'class': 'form-control'}),
    'no_of_positions': forms.NumberInput(attrs={'class': 'form-control'}),
    'location': forms.TextInput(attrs={'class': 'form-control'}),
    'company_name': forms.TextInput(attrs={'class': 'form-control'}),
    'company_disc': forms.TextInput(attrs={'class': 'form-control'}),
    'salary': forms.TextInput(attrs={'class': 'form-control'}),
    'salary_type': forms.Select(attrs={'class': 'p-2 mt-4'}),
    'job_requirement': forms.TextInput(attrs={'class': 'form-control'}),
    'job_qualifications': forms.TextInput(attrs={'class': 'form-control'}),
    'job_skills': forms.TextInput(attrs={'class': 'form-control'}),
    'job_description': forms.TextInput(attrs={'class': 'form-control'}),
    'last_date_to_apply': forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }),
    'domain': forms.TextInput(attrs={'class': 'form-control'}),
}

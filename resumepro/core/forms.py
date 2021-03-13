from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('male', 'male'),
    ('Female', 'Female')
]
JOB_CHOICES = [
    ('PUNE', 'PUNE'),
    ('MUMBAI', 'MUMBAI'),
    ('BANGALURU','BANGALURU')
]    


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='prferred job Locations', choices=JOB_CHOICES,widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Resume
        fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'profile_img', 'my_file']
        labels = {'name': 'Full Name', 'dob': 'Date of Birth', 'email': 'Email id'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control','id':'datepicker'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'job_city': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
import email
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(initial='Sonam')
    email = forms.EmailField()
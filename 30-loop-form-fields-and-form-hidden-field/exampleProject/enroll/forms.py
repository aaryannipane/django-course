import email
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # hidden field
    key = forms.CharField(widget=forms.HiddenInput())
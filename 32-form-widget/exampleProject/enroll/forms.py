import email
from django import forms

class StudentRegistration(forms.Form):

    name = forms.CharField()

    password = forms.CharField(widget=forms.PasswordInput())

    hidden = forms.CharField(widget=forms.HiddenInput())

    textArea = forms.CharField(widget=forms.Textarea())

    checkBox = forms.CharField(widget=forms.CheckboxInput())

    fileInput = forms.CharField(widget=forms.FileInput())

    # attr 
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'helptext', 'id':'uniqueid'}))



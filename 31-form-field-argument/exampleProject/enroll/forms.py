import email
from django import forms

class StudentRegistration(forms.Form):
    # change label name
    name = forms.CharField(label='Your name')

    # change label sufix
    email = forms.CharField(label_suffix=' = ')

    # give initial value 
    initial_Value = forms.CharField(initial='Jhon Doe')

    # remove required
    no_required = forms.CharField(required=False)

    # disabled field 
    disable_field = forms.CharField(disabled=True)

    # give help text
    help_text = forms.CharField(help_text='Only Char Allowed')

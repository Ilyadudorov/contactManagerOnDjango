from django import forms
from django.core.validators import RegexValidator

class UserForm(forms.Form):
    name = forms.CharField(max_length=20)
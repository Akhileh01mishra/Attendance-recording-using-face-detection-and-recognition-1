from crispy_forms.helper import FormHelper
from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20,required=True)
    inputPassword=forms.PasswordInput(max_length=20)
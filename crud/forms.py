from django.contrib.auth.forms import PasswordResetForm
from django import forms

class Custom(PasswordResetForm):
    email = forms.EmailField(max_length=254,widget=forms.EmailInput(attrs={"placeholder": "email"}))
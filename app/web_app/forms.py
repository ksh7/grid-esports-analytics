from django import forms

from . import models

class LoginForm(forms.Form):
    email = forms.CharField(label="Email", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    about = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    
    class Meta:
        model = models.User
        fields = ['email', 'password', 'name']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'password': 'Password',
        }

# class RegisterForm(forms.Form):
#     email = forms.CharField(label="Email", max_length=100)
#     password = forms.CharField(label="Password", widget=forms.PasswordInput)
#     about = forms.CharField(label="About")

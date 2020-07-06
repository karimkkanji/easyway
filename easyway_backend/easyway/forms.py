from django import forms
from .models import customers
from django.contrib.auth.forms import AuthenticationForm

class customersForm(forms.ModelForm):
	model = customers
	username = forms.CharField(label='Username',max_length = 30)
	profile_pic = forms.ImageField(label = 'Image Field')

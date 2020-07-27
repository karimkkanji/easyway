from django import forms
from .models import *
# from django.contrib.auth.forms import AuthenticationForm

class customersForm(forms.ModelForm):
	firstname=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Name'}))
	lastname=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Name'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'size':30,'placeholder':'Type your password'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'size':50,'placeholder':'Enter Email Address'}))
	phonenumber= forms.CharField(widget=forms.TextInput(attrs={'size':13,'placeholder':'Enter your phone number'}))
	AccountNumber=forms.CharField(widget=forms.TextInput(attrs={'size':15,'placeholder':'1343*******6756'}))
	profile_pic = forms.ImageField(label = 'Profile Pic')
	class Meta:
		model = user
		fields = ('firstname','lastname','email','password','phonenumber','AccountNumber','profile_pic')

# class packagesForm(forms.ModelForm):
# 	package_id=forms.ModelChoiceField(queryset=user.objects.all(),initial='')
# 	class Meta:
# 		model = packages
# 		fields = ('package_id',)

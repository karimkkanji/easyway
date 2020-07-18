from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class customersForm(forms.ModelForm):
	model = customers
	username = models.CharField(default='User',max_length=30)
	user = models.ForeignKey(User,on_delete = models.SET_NULL, null=True)
	activity_title = models.ForeignKey('activities', on_delete = models.SET_NULL, null=True)
	profile_pic = models.ImageField(upload_to = "profile/",null=True)
	first_name = models.CharField(max_length =30)
	last_name = models.CharField(max_length =30)
	email = models.EmailField(max_length =50)
	phonenumber = models.IntegerField()
	AccountNumber = models.IntegerField()

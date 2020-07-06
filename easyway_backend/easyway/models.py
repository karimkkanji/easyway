from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customers(models.Model):
	username = models.CharField(default='User',max_length=30)
	# profile_pic = models.ImageField(upload_to = "profile/",null=True)
	first_name = models.CharField(max_length =30)
	last_name = models.CharField(max_length =30)
	email = models.EmailField(max_length =50)
	phonenumber = models.IntegerField()
	AccountNumber = models.IntegerField()

	def __str__(self):
		return self.username

	def delete_profile(self):
		self.delete()

	def save_profile(self):
		self.save()

class hotel(models.Model):
	No_of_guests = models.IntegerField(8)
	No_of_bedrooms = models.IntegerField(8)
	No_of_beds = models.IntegerField(8)
	No_of_baths = models.IntegerField(8)
	No_of_toilets = models.IntegerField(8)
	more_details = models.TextField(max_length =200)
	# location = models.GoogleMap()
	checkin = models.TimeField(auto_now_add = True)
	checkout = models.TimeField(auto_now_add = True)
	discount_per_person = models.SmallIntegerField(50)
	group_discount_per_person = models.SmallIntegerField(50)


class rent_car(models.Model):
	car_model = models.CharField(max_length = 200)
	# add_photos = models.ImageField(upload_to = "cars/",null=True)
	more_details = models.TextField(max_length = 200)
	# location = models.GoogleMap()
	place_available = models.TextField(20)
	discount_per_person = models.SmallIntegerField(50)

class activities(models.Model):
	activity_title = models.TextField(max_length = 20)
	# location = models.GoogleMap()
	days = models.DateTimeField()
	opening_hours = models.DateTimeField()
	age = models.IntegerField()
	max_persons = models.IntegerField() 
	discount_per_person = models.SmallIntegerField(50)
	group_discount_per_person = models.SmallIntegerField(50)

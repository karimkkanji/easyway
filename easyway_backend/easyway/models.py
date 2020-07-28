from django.db import models
# from django_google_maps import fields as map_fields
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager,User
# Create your models here.
class usermanager(BaseUserManager):
	def create_user(self,email,password,firstname):
		user=self.model(email=email,password=password,firstname=firstname)
		user.set_password(password, null=True)
		user.is_staff=False
		user.is_superuser=False
		user.save(using=self._db)
		return user
	def create_superuser(self,email,password,firstname):
		user=self.create_user(email=email,password=password,firstname=firstname,lastname=lastname)
		user.is_active=True
		user.is_staff=True
		user.is_superuser=True
		user.save(using=self._db)
		return user 


class user(AbstractBaseUser,PermissionsMixin):
	profile_pic = models.ImageField(upload_to = "profile/",null=True)
	firstname = models.CharField(max_length =30)
	lastname = models.CharField(max_length =30)
	email = models.EmailField(max_length =50, unique=True)
	phonenumber = models.CharField(max_length=13)
	AccountNumber = models.CharField(max_length=15)
	is_staff=models.BooleanField(default=False)
	is_superuser=models.BooleanField(default=False)
	is_active=models.BooleanField(default=True)
	USERNAME_FIELD='email'
	REQUIRED_FIELDS=['firstname','lastname','AccountNumber','phonenumber']

	objects=usermanager()

	def __str__(self):
		return self.email
	def get_short_name(self):
		return self.email

class activities(models.Model):
	activity_title = models.TextField(max_length = 20)
	# address = map_fields.AddressField(max_length=200, blank=True, null=True)
	# geolocation = map_fields.GeoLocationField(max_length=100, blank=True, null=True)
	days = models.DateTimeField()
	opening_hours = models.DateTimeField()
	age = models.CharField(max_length=3)
	max_persons = models.CharField(max_length=20) 
	discount_per_person = models.CharField(max_length=50)
	group_discount_per_person = models.CharField(max_length=50)
	email = models.ForeignKey(user, on_delete = models.SET_NULL, null=True)

class hotel(models.Model):
	name = models.CharField(max_length = 20, null=True)
	guests = models.CharField(max_length=8)
	bedrooms = models.CharField(max_length=8)
	beds = models.CharField(max_length=8)
	baths = models.CharField(max_length=8)
	toilets = models.CharField(max_length=8)
	more_details = models.TextField(max_length =200)
	# address = map_fields.AddressField(max_length=200, blank=True, null=True)
	# geolocation = map_fields.GeoLocationField(max_length=100,blank=True, null=True)
	checkin = models.TimeField(auto_now_add = True)
	checkout = models.TimeField(auto_now_add = True)
	discount_per_person = models.CharField(max_length=50)
	group_discount_per_person = models.CharField(max_length=50)
	activity_title = models.ForeignKey(activities,on_delete = models.SET_NULL,  null=True)
	email = models.ForeignKey(user,on_delete = models.SET_NULL, null=True)


class rent_car(models.Model):
	car_model = models.CharField(max_length = 200)
	add_photos = models.ImageField(upload_to = "cars/",null=True)
	more_details = models.TextField(max_length = 200)
	# address = map_fields.AddressField(max_length=200,blank=True, null=True)
	# geolocation = map_fields.GeoLocationField(max_length=100,blank=True, null=True)
	place_available = models.TextField(20)
	discount_per_person = models.CharField(max_length=50)
	activity_title = models.ForeignKey(activities, on_delete = models.SET_NULL, null=True)


class packages(models.Model):
	package_id = models.CharField(max_length = 20, null=True)
	activity_title = models.ForeignKey(activities, on_delete= models.SET_NULL,null=True)
	car_model = models.ForeignKey(rent_car, on_delete = models.SET_NULL, null=True)
	car_model = models.ForeignKey(rent_car, on_delete = models.SET_NULL, null=True)
	name = models.ForeignKey(hotel, on_delete=models.SET_NULL, null=True)
	email = models.ForeignKey(user, on_delete = models.SET_NULL, null=True)

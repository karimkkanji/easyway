from rest_framework import serializers
from .models import *


class HotelSerializer(serializers.ModelSerializer):

	class Meta:
		model = hotel
		fields = '__all__' 


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = customers
        # fields = ('pk','username','first_name', 'last_name', 'email', 'phonenumber','AccountNumber','profile_pic ')
        fields = '__all__' 

class RentCarSerializer(serializers.ModelSerializer):

	class Meta:
		model = rent_car
		fields = '__all__' 

class ActivitiesSerializer(serializers.ModelSerializer):

	class Meta:
		model = activities
		fields = '__all__' 

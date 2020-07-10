from rest_framework import serializers
from .models import customers

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = customers
        fields = ('pk','username','first_name', 'last_name', 'email', 'phonenumber','AccountNumber')

from django.shortcuts import render, redirect
from django.http  import HttpResponse

# Create your views here.
def index(request):
	return render(request, "index.html")

def hotels(request):
    return render(request, "hotel.html")

def rent_cars(request):
    return render(request, "rent-a-car.html")

def activities(request):
    return render(request, "activities.html")

def bungalow(request):
    return render(request, "bungalow.html")

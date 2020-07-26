from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
	return render(request, "index.html")

@login_required(login_url='/accounts/login/')
def hotels(request):
    return render(request, "hotel.html")

@login_required(login_url='/accounts/login/')
def rent_cars(request):
    return render(request, "rent-a-car.html")

@login_required(login_url='/accounts/login/')
def activities(request):
    return render(request, "activities.html")

@login_required(login_url='/accounts/login/')
def bungalow(request):
    return render(request, "bungalow.html")

@login_required(login_url='/accounts/login/')
def calendar_reserv(request):
    return render(request, "calendar-reservations.html")

@login_required(login_url='/accounts/login/')
def create_mypackage(request):
    return render(request, "my-packages-created.html")

@login_required(login_url='/accounts/login/')
def confirm_mypackage(request):
    return render(request, "my-packages-confirmed.html")

@login_required(login_url='/accounts/login/')
def my_reservations(request):
    return render(request, "my-reservations.html")

@login_required(login_url='/accounts/login/')
def activities_1(request):
	return render(request, "activities-1.html")

@login_required(login_url='/accounts/login/')
def bungalow_1(request):
    return render(request, "bungalow-1.html")

@login_required(login_url='/accounts/login/')
def create_activity(request):
    return render(request, "create-activity.html")

@login_required(login_url='/accounts/login/')
def create_bungalow(request):
    return render(request, "create-bungalow.html")

@login_required(login_url='/accounts/login/')
def create_car(request):
    return render(request, "create-car.html")

@login_required(login_url='/accounts/login/')
def create_event(request):
    return render(request, "create-event.html")

@login_required(login_url='/accounts/login/')
def create_hotel(request):
    return render(request, "create-hotel.html")
@login_required(login_url='/accounts/login/')
def create_packages(request):
    return render(request, "packages-created.html")

@login_required(login_url='/accounts/login/')
def confirmed_packages(request):
    return render(request, "packages-confirmed.html")

@login_required(login_url='/accounts/login/')
def rent_a_car(request):
	return render(request, "rent-a-car-1.html")

@login_required(login_url='/accounts/login/')
def rent_car_details(request):
    return render(request, "rent-a-car-details.html")

@login_required(login_url='/accounts/login/')
def event_2(request):
    return render(request, "event-2.html")

@login_required(login_url='/accounts/login/')
def event_3(request):
    return render(request, "event-3.html")

@login_required(login_url='/accounts/login/')
def bungalow_1(request):
    return render(request, "bungalow-1.html")

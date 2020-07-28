from django.shortcuts import render, redirect
from django.http  import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login, logout

# @login_required
def index(request):
	return render(request, "index.html")

def signup(request):
    if request.method == 'POST':
        form = customersForm(request.POST)       
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()        
            return redirect('index')
    else:
        form = customersForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def special(request):
    return HttpResponse("You are logged in !")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html', {})

def hotels(request):
    return render(request, "hotel.html")

def rent_cars(request):
    return render(request, "rent-a-car.html")

def activities(request):
    return render(request, "activities.html")

def bungalow(request):
    return render(request, "bungalow.html")

def calendar_reserv(request):
    return render(request, "calendar-reservations.html")


def create_mypackage(request):
    return render(request, "my-packages-created.html")

def confirm_mypackage(request):
    return render(request, "my-packages-confirmed.html")


def my_reservations(request):
    return render(request, "my-reservations.html")


def activities_1(request):
	return render(request, "activities-1.html")


def bungalow_1(request):
    return render(request, "bungalow-1.html")


def create_activity(request):
    return render(request, "create-activity.html")

def create_bungalow(request):
    return render(request, "create-bungalow.html")


def create_car(request):
    return render(request, "create-car.html")

def create_event(request):
    return render(request, "create-event.html")


def create_hotel(request):
    return render(request, "create-hotel.html")

def create_packages(request):
    return render(request, "packages-created.html")


def confirmed_packages(request):
    return render(request, "packages-confirmed.html")


def rent_a_car(request):
	return render(request, "rent-a-car-1.html")


def rent_car_details(request):
    return render(request, "rent-a-car-details.html")


def event_2(request):
    return render(request, "event-2.html")

def event_3(request):
    return render(request, "event-3.html")

def bungalow_1(request):
    return render(request, "bungalow-1.html")

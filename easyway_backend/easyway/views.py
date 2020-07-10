from django.shortcuts import render, redirect
# from django.http  import HttpResponse

# # Create your views here.
# def index(request):
# 	return render(request, "index.html")

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import customers
from .serializers import *

def index(request):
    return render(request, 'index.html')

@api_view(['GET', 'POST'])
def customers_list(request, *args, **kwargs):
    global customers
    """
    List  customers, or create a new customer.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        customers = customers.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 5)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = CustomerSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/customers/?page=' + str(nextPage), 'prevlink': '/api/customers/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def customers_detail(request, pk):
    """
    Retrieve, update or delete a customer by id/pk.
    """
    try:
        customers = customers.objects.get(pk=pk)
    except customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customers,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customers, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def hotel_list(request, *args, **kwargs):
    global hotel
    """
    List  hotel, or create a new customer.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        hotel = hotel.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(hotel, 5)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = HotelSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/hotel/?page=' + str(nextPage), 'prevlink': '/api/hotel/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def hotel_detail(request, pk):
    """
    Retrieve, update or delete a hotel by id/pk.
    """
    try:
        hotel = hotel.objects.get(pk=pk)
    except customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(hotel,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(hotel, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def rent_car_list(request, *args, **kwargs):
    global rent_car
    """
    List  Rent cars, or create a new customer.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        rent_car = rent_car.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(rent_car, 5)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = RentCarSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/rent_car/?page=' + str(nextPage), 'prevlink': '/api/rent_car/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = RentCarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def rent_car_detail(request, pk):
    """
    Retrieve, update or delete a hotel by id/pk.
    """
    try:
        rent_car = rent_car.objects.get(pk=pk)
    except customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RentCarSerializer(rent_car,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(rent_car, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        rent_car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def activities_list(request, *args, **kwargs):
    global activities
    """
    List  Activities, or create a new activities.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        activities = activities.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(activities, 5)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = ActivitiesSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/activities/?page=' + str(nextPage), 'prevlink': '/api/activities/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = ActivitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def activities_detail(request, pk):
    """
    Retrieve, update or delete a activity by id/pk.
    """
    try:
        activities = activities.objects.get(pk=pk)
    except activities.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActivitiesSerializer(activities,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ActivitiesSerializer(activities, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        activities.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

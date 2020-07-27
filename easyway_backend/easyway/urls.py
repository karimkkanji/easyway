from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url(r'^$', views.login_redirect, name='login_redirect'),
    url('^$',views.index, name='index'),
    url(r'^hotels/$', views.hotels, name='hotels'),
    url(r'^rent_cars/$', views.rent_cars, name='rent_cars'),
    url(r'^activities/$', views.activities, name='activities'),
    url(r'^bungalow/$', views.bungalow, name='bungalow'),
    url(r'^calendar_reserv/$', views.calendar_reserv, name='calendar_reserv'),
    url(r'^create_mypackage/$', views.create_mypackage, name='create_mypackage'),
    url(r'^confirm_mypackage/$', views.confirm_mypackage, name='confirm_mypackage'),
    url(r'^my_reservations/$', views.my_reservations, name='my_reservations'),
    url(r'^activities_1/$', views.activities_1, name='activities_1'),
    url(r'^bungalow_1/$', views.bungalow_1, name='bungalow_1'),
    url(r'^create_activity/$', views.create_activity, name='create_activity'),
    url(r'^create_bungalow/$', views.create_bungalow, name='create_bungalow'),
    url(r'^create_car/$', views.create_car, name='create_car'),
    url(r'^create_event/$', views.create_event, name='create_event'),
    url(r'^create_hotel/$', views.create_hotel, name='create_hotel'),
    url(r'^create_packages/$', views.create_packages, name='create_packages'),
    url(r'^confirmed_packages/$', views.confirmed_packages, name='confirmed_packages'),
    url(r'^rent_a_car/$', views.rent_a_car, name='rent_a_car'),
    url(r'^rent_car_details/$', views.rent_car_details, name='rent_car_details'),
    url(r'^event_2/$', views.event_2, name='event_2'),
    url(r'^event_3/$', views.event_3, name='event_3'),
    url(r'^bungalow_1/$', views.bungalow_1, name='bungalow_1'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'special/',views.special,name='special'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

    ]

if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 


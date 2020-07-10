"""easyway_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth import views as auth_views

from easyway import views



urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^api/customers/$', views.customers_list),
    url(r'^api/customers/(?P<pk>[0-9]+)$', views.customers_detail),
    url(r'^api/hotel/$', views.hotel_list),
    url(r'^api/hotel/(?P<pk>[0-9]+)$', views.hotel_detail),
    url(r'^api/rent_car/$', views.rent_car_list),
    url(r'^api/rent_car/(?P<pk>[0-9]+)$', views.rent_car_detail),
    url(r'^api/activities/$', views.activities_list),
    url(r'^api/activities/(?P<pk>[0-9]+)$', views.activities_detail),
    # url(r'^tinymce/', include('tinymce.urls')),
    url(r'',include('easyway.urls')),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
    # url( r'^login/$',auth_views.LoginView.as_view, name="login"),
    # url(r'^logout/$', auth_views.LogoutView.as_view, {"next_page": '/'}),
]

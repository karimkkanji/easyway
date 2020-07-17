from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index, name='index'),
    url(r'^hotels/$', views.hotels, name='hotels'),
    url(r'^rent_cars/$', views.rent_cars, name='rent_cars'),
    url(r'^activities/$', views.activities, name='activities'),
    url(r'^bungalow/$', views.bungalow, name='bungalow'),
    ]
if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 


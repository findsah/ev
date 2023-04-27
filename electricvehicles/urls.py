"""electricvehicles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from electric_vehicles.views import electric_vehicle_details, electric_vehicle_make_model_split, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('electric_vehicle_make_model_split/', electric_vehicle_make_model_split, name='electric_vehicle_make_model_split'), 
    path('electric-vehicles-search/<str:vin>/', electric_vehicle_details, name='electric_vehicle_detail'),


]

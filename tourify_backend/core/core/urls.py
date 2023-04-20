"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tourist_spot/',include('aplications.tourist_spot.urls')),
    path('api/tourist_spot/',include('aplications.tourist_spot.urls')),
    path('api/auth/',include('aplications.authentication.urls')),
    path('api/tour_guide/',include('aplications.tour_guide.urls')),
    path('api/user_tour/',include('aplications.user_tour.urls'))
]

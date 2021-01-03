"""mainsite URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('guess_the_r_number/', include('guess_the_r_number.urls')),
    path('covidstats/', include('charts.urls')),
    path('schitter/', include('schitter.urls')),
    path('chartjs/', include('chartjs.urls')),
    path('charts/', include('charts.urls')),
    path('LeafletMaps/', include('LeafletMaps.urls')),
    path('highcharts/', include('highcharts.urls')),
    path('go_test/', include('go_test.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

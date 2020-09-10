from django.urls import path

from . import views

urlpatterns = [
    path('', views.CreateChart, name='chart'),
    path('Test', views.Test, name='test'),
    path('daily_confirmed_total_confirmed', views.daily_confirmed_total_confirmed, name='daily_confirmed_total_confirmed'),
]

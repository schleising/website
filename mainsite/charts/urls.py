from django.urls import path

from . import views

urlpatterns = [
    path('', views.CreateChart, name='chart'),
    path('Test', views.Test, name='test'),
]
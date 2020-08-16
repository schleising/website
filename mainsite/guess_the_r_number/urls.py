from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='guess_the_r_number'),
]

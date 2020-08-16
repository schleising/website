from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='schitter'),
    path('take_a_schitt/', views.take_a_schitt, name='take_a_schitt'),
    path('log_schitt/', views.log_schitt, name='log_schitt'),
]

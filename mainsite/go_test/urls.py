from django.urls import path

from . import views

urlpatterns = [
    path('', views.go_test, name='go_test'),
    path('canvas', views.go_canvas, name='go_canvas'),
]

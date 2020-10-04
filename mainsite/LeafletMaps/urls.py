from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='LeafletMaps'),
    path('uk_cumulative_cases', views.uk_cumulative_cases, name='uk_cumulative_cases'),
]

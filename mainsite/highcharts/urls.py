from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='highcharts'),
    path('new_cases_bar_chart', views.NewCasesBarChart, name='new_cases_bar_chart'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='highcharts'),
    path('new_cases_bar_chart', views.NewCasesBarChart, name='new_cases_bar_chart'),
    path('global_new_cases', views.NewCasesAgainstTime, name='global_new_cases'),
    path('checkbox_clicked', views.CheckboxClicked, name='checkbox_clicked'),
]

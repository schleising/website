from django.urls import path

from . import views

urlpatterns = [
    path('', views.CreateChart, name='chart'),
    path('Test', views.Test, name='test'),
    path('daily_confirmed_total_confirmed', views.daily_confirmed_total_confirmed, name='daily_confirmed_total_confirmed'),
    path('daily_confirmed_vs_time', views.daily_confirmed_vs_time, name='daily_confirmed_vs_time'),
    path('active_cases_vs_time', views.active_cases_vs_time, name='active_cases_vs_time'),
    path('deaths_vs_time', views.deaths_vs_time, name='deaths_vs_time'),
    path('total_deaths_since_first', views.total_deaths_since_first, name='total_deaths_since_first'),
    path('daily_deaths_since_first', views.daily_deaths_since_first, name='daily_deaths_since_first'),
    path('country_stats', views.country_stats, name='country_stats'),
    path('deaths_against_time_bar', views.deaths_against_time_bar, name='deaths_against_time_bar'),
]

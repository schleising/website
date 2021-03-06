from django.urls import path

from . import views

urlpatterns = [
    # path('', views.daily_confirmed_total_confirmed, name='daily_confirmed_total_confirmed'),
    path('global_new_cases', views.NewCasesAgainstTime, name='global_new_cases'),
    path('global_deaths', views.DeathsAgainstTime, name='global_deaths'),
    path('daily_cases_total_cases', views.DailyCasesAgainstTotalCases, name='daily_cases_total_cases'),
    path('checkbox_clicked', views.CheckboxClicked, name='checkbox_clicked'),
]

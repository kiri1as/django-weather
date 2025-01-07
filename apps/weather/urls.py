from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage_view, name='weather-home'),
    path('weather/current', views.weather_page_view, name='weather-current'),
    path('weather/history', views.weather_history_view, name='weather-history'),
    path('logout/', views.logout_view, name='logout'),
]

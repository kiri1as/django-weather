import os

import requests
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.response import TemplateResponse

from weathersite.utils import AllowedMethods
from .forms import CityForm
from .models import WeatherHistory


@AllowedMethods(['GET'])
def homepage_view(request: HttpRequest) -> HttpResponse:
    project_name = os.getenv('PROJECT_NAME')
    return TemplateResponse(
        request=request,
        template='home_page.html',
        context={'base_title': project_name, 'page_title': 'Home Page', 'project_name': project_name}
    )


@AllowedMethods(['GET', 'POST'])
@login_required
def weather_page_view(request):
    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = os.getenv('API_KEY')
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=en'
            response = requests.get(url)
            weather_data = response.json()

            if weather_data.get('cod') == 200:
                weather_history = WeatherHistory(
                    user=request.user,
                    city=city,
                    temperature=weather_data['main']['temp'],
                    description=weather_data['weather'][0]['description'],
                    humidity=weather_data['main']['humidity'],
                    wind_speed=weather_data['wind']['speed']
                )
                weather_history.save()
            context = {
                'weather_data': weather_data,
                'form': form
            }
            return render(request, 'weather_page.html', context)
    else:
        form = CityForm()
    return render(request, 'weather_page.html',
                  {'form': form, 'page_title': 'Current Weather', 'base_title': os.getenv('PROJECT_NAME')})


@login_required
def weather_history_view(request):
    history = WeatherHistory.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(history, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'weather_history_page.html',
                  {'page_obj': page_obj, 'page_title': 'Request history', 'base_title': os.getenv('PROJECT_NAME')})


@AllowedMethods(['GET', 'POST'])
@login_required
def logout_view(request):
    logout(request)
    return redirect('weather-home')

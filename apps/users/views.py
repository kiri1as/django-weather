from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import UserRegistrationForm
from weathersite.utils import AllowedMethods


@AllowedMethods(['GET', 'POST'])
def register_user_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'user_registration.html', {'form': form})


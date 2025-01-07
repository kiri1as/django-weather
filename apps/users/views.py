import os

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.defaultfilters import title

from weathersite.utils import AllowedMethods
from .forms import UserRegistrationForm, UserLoginForm


@AllowedMethods(['GET', 'POST'])
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account have been created, {username}! Now you can login.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user_registration.html',
                  {'form': form, 'base_title': os.getenv('PROJECT_NAME'), 'title': 'Account creation'})


@AllowedMethods(['GET', 'POST'])
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password!')
        else:
            messages.error(request, 'Invalid data')
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html',
                  {'form': form, 'base_title': os.getenv('PROJECT_NAME'), 'title': 'Login page'})

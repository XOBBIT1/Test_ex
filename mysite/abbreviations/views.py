import string
from random import random

import pyshorteners
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

def index(request):
    return render(request, 'abbreviations/abbreviations.html')


def shorten(request, url):
    shortened_url_hash = service.shorten(url)
    shortened_url = request.build_absolute_uri(reverse('redirect', args=[shortened_url_hash]))
    return render(request, 'main/link.html', {'shortened_url': shortened_url})


def shorten_post(request):
    return shorten(request, request.POST['url'])

def redirect_hash(request, url_hash):
    original_url = service.load_url(url_hash).original_url
    return redirect(original_url)

def login_user(request):
    if request. method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile_detail')
        else:
            messages.success(request, ("Не правильно введён логин или пароль!!! Попробуйте снова..."))
            return redirect('login')
    else:
        return render(request, 'abbreviations/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Вы успешно вышли из аккаунта"))
    return redirect('/')


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Регистрация прошла успешно!!!'))
            return redirect('abbreviations/abbreviations.html')
    else:
        form = UserCreationForm()
    return render(request, "abbreviations/registration.html", {
        'form': form,
    })
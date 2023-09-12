from datetime import datetime
import os
import json
import random
import string

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from wsgiref.util import FileWrapper
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse

from . import models
from . import forms
from . import gpt

matches_data = []
with open(os.path.abspath(os.path.dirname(__file__)) + '/matches.json', 'r') as json_obj:
    matches_data = json.loads(json_obj.read())

def index(request):
    context = {'matches': matches_data}
    return render(request, 'web_app/index.html', context)


def game_stream(request, stream_id=0):
    context = {"stream_id": stream_id, 'matches': matches_data}
    return render(request, 'web_app/game_stream.html', context)


def chat_gpt_prompt_select(request):
    if request.method == 'POST':
        prompt_id = request.POST.get('analyticsPrompt', 0)
        data_set = request.POST.get('roundDataSet', {})
        response = gpt.gpt_api(int(prompt_id), data_set)
        return JsonResponse({"result": response})


def live_games(request):
    context = {'matches': matches_data}
    return render(request, 'web_app/live_games.html', context)


def download_reports(request):
    context = {'matches': matches_data}
    return render(request, 'web_app/download_reports.html', context)


@login_required
def dashboard(request):
    context = {'matches': matches_data}
    return render(request, 'web_app/dashboard.html', context)


def registerUser(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('dashboard')  # Change 'home' to your desired redirect URL
    else:
        form = forms.RegistrationForm()
    
    context = {'form': form}
    return render(request, 'web_app/register.html', context)


def favicon_ico(request):
    favicon_path = os.path.join(settings.BASE_DIR, 'static', 'favicon.ico')
    return serve(request, os.path.basename(favicon_path), os.path.dirname(favicon_path))


def loginUser(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Change 'home' to your desired redirect URL
            else:
                form.add_error(None, "Email OR password is incorrect.")
    else:
        form = forms.LoginForm()
    
    context = {'form': form, 'matches': matches_data}
    return render(request, 'web_app/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')
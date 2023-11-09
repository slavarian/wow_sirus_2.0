from django.shortcuts import render , redirect
from django.shortcuts import render, get_object_or_404
from .forms.login_form import LoginForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .forms.reg_form import RegistrationForm
from django.contrib.auth import login, authenticate
from .models import MyUser
from .models import Character
from django.db.models.query import QuerySet
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    user_account = request.user 
    return render(request, 'profile.html', {'user_account': user_account})

def character_info(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    return render(request, 'character_info.html', {'character': character})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile') 
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile') 
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
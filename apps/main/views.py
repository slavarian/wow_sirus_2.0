from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.

def main(request):
    template_name = "main.html"
    return render(request , template_name)

@login_required
def profile(request):
    return render(request, 'profile.html')

def custom_logout(request):
    logout(request)
    return redirect('main_page')
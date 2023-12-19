from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from auths.models import MyUser

def main(request):
    user_count = MyUser.objects.count()
    context = {'user_count': user_count}
    template_name = "main.html"
    return render(request, template_name, context)

@login_required
def profile(request):
    return render(request, 'profile.html')

def custom_logout(request):
    logout(request)
    return redirect('main_page')
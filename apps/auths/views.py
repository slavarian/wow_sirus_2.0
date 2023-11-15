from django.shortcuts import render , redirect
from django.shortcuts import render, get_object_or_404
from .forms.login_form import LoginForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .forms.reg_form import RegistrationForm
from django.contrib.auth import login, authenticate
from .models import MyUser
from .models import Character
from wow_db.models import Body_armor
from django.db.models.query import QuerySet
from django.contrib.auth.decorators import login_required
from .forms.character_form import GameCharacterForm
from django.http import JsonResponse
from django.views.decorators.http import require_GET

@login_required
def profile(request):
    user_account = request.user 
    characters = Character.objects.filter(user=request.user)
    return render(request, 'profile.html', {'user_account': user_account , 'characters': characters})

def character_info(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    body_armors = Body_armor.objects.all()  # Adjust this query based on your needs
    return render(request, 'character_info.html', {'character': character, 'body_armors': body_armors})


def equip_gear(request):
    if request.method == 'POST':
        character_id = request.POST.get('character_id')
        gear_type = request.POST.get('gear_type')
        selected_item_id = request.POST.get('selected_item')
        character = Character.objects.get(id=character_id)
        selected_item = Body_armor.objects.get(id=selected_item_id)
        if gear_type == 'bodyArmor':
            character.equip_body_armor(selected_item)

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Неверный запрос'})

def create_character(request):
    if request.method == 'POST':
        form = GameCharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user
            character.save()
            return redirect('profile')  
    else:
        form = GameCharacterForm()

    return render(request, 'create_character.html', {'form': form})

@require_GET
def get_races(request):
    fraction = request.GET.get('fraction', None)
    if fraction == 'Horde':
        races = {'Orc': 'Орк', 'Troll': 'Троль','Bood Elf':'Эльф крови','Undead':'Нежить','Tauren':'Корова','Goblin':'Гоблин','Pandaren':'Панда'}
    elif fraction == 'Alliance':
        races = {'Human': 'Человек', 'Dwarf': 'Дворф','Night Elf':'Ночной эльф','Gnome':'Гном','Dwarf':'Дворф','Worgen':'Ворген','Draeneir':'Дреней','Pandaren':'Панда'}

    return JsonResponse(races)

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

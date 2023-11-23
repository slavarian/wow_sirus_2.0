from django.shortcuts import render , redirect
from django.shortcuts import render, get_object_or_404
from .forms.login_form import LoginForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .forms.reg_form import RegistrationForm
from django.contrib.auth import login, authenticate
from .models import MyUser
from .models import Character
from wow_db.models import (Body_armor , Head_armor , Boots_armor ,
                           Gloves_armor , Legs_armor ,Back_armor,
                            Shoulder_armor , Wrist_armor , Belt_armor,
                            Ring , Trinket , Weapon , Amulet  )
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
    body_armors = Body_armor.objects.all()
    head_armors = Head_armor.objects.all()
    boots_armor = Boots_armor.objects.all() 
    gloves_armor = Gloves_armor.objects.all() 
    back_armor = Back_armor.objects.all() 
    shoulder_armor = Shoulder_armor.objects.all() 
    belt_armor = Belt_armor.objects.all() 
    ring = Ring.objects.all() 
    trinket = Trinket.objects.all() 
    weapon = Weapon.objects.all() 
    amulet = Amulet.objects.all() 
    wrist_armor = Wrist_armor.objects.all() 
    legs_armor = Legs_armor.objects.all()   
    return render(request, 'character_info.html', {'character': character, 'body_armors': body_armors ,
            'head_armors':head_armors,'boots_armor':boots_armor,'gloves_armor':gloves_armor,'back_armor':back_armor,
            'shoulder_armor':shoulder_armor,'belt_armor':belt_armor,'ring':ring,'trinket':trinket,
            'weapon':weapon,'amulet':amulet,'wrist_armor':wrist_armor,'legs_armor':legs_armor})


def equip_gear(request):
    if request.method == 'POST':
        character_id = request.POST.get('character_id')
        gear_type = request.POST.get('gear_type')
        selected_item_id = request.POST.get('selected_item')
        character = Character.objects.get(id=character_id)
        armor_model = get_armor_model(gear_type)
        
        try:
            selected_item = armor_model.objects.get(id=selected_item_id)
        except armor_model.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Выбранный предмет не найден'})
        
        if gear_type == 'bodyArmor':
            character.equip_body_armor(selected_item)
        elif gear_type == 'headArmor':
            character.equip_head_armor(selected_item)
        elif gear_type == 'bootsArmor':
            character.equip_boots_armor(selected_item)
        elif gear_type == 'glovesArmor':
            character.equip_gloves_armor(selected_item)
        elif gear_type == 'legsArmor':
            character.equip_legs_armor(selected_item)
        elif gear_type == 'backArmor':
            character.equip_back_armor(selected_item)
        elif gear_type == 'shoulderArmor':
            character.equip_shoulder_armor(selected_item)
        elif gear_type == 'wristArmor':
            character.equip_wrist_armor(selected_item)
        elif gear_type == 'beltArmor':
            character.equip_belt_armor(selected_item)
        elif gear_type == 'ringSlot':
            character.equip_ring(selected_item)
        elif gear_type == 'amulet':
            character.equip_amulet(selected_item)
        elif gear_type == 'trinketSlot':
            character.equip_trinket(selected_item)
        elif gear_type == 'weaponSlot':
            character.equip_weapon(selected_item)

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'error': 'Неверный запрос'})

def get_armor_model(gear_type):
    if gear_type == 'bodyArmor':
        return Body_armor
    elif gear_type == 'headArmor':
        return Head_armor
    elif gear_type == 'bootsArmor':
        return Boots_armor
    elif gear_type == 'glovesArmor':
        return Gloves_armor
    elif gear_type == 'legsArmor':
        return Legs_armor
    elif gear_type == 'backArmor':
        return Back_armor
    elif gear_type == 'shoulderArmor':
        return Shoulder_armor
    elif gear_type == 'wristArmor':
        return Wrist_armor
    elif gear_type == 'beltArmor':
        return Belt_armor
    elif gear_type == 'ringSlot':
        return Ring
    elif gear_type == 'amulet':
        return Amulet
    elif gear_type == 'trinketSlot':
        return Trinket
    elif gear_type == 'weaponSlot':
        return Weapon



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

from django.shortcuts import render , redirect
from django.shortcuts import render, get_object_or_404
from .forms.login_form import LoginForm
from django.http.request import HttpRequest
from django.http.response import HttpResponse , HttpResponseRedirect
from .forms.reg_form import RegistrationForm
from django.contrib.auth import login, authenticate
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
from django.urls import reverse


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
    ring1 = Ring.objects.all() 
    ring2 = Ring.objects.all() 
    trinket1 = Trinket.objects.all()
    trinket2 = Trinket.objects.all()  
    weapon1 = Weapon.objects.all()
    weapon2 = Weapon.objects.all()  
    amulet = Amulet.objects.all() 
    wrist_armor = Wrist_armor.objects.all() 
    legs_armor = Legs_armor.objects.all()   
    return render(request, 'character_info.html', {'character': character, 'body_armors': body_armors ,
            'head_armors':head_armors,'boots_armor':boots_armor,'gloves_armor':gloves_armor,'back_armor':back_armor,
            'shoulder_armor':shoulder_armor,'belt_armor':belt_armor,'ring1':ring1,'trinket1':trinket1,'ring2':ring2,'trinket2':trinket2,
            'weapon1':weapon1,'weapon2':weapon2,'amulet':amulet,'wrist_armor':wrist_armor,'legs_armor':legs_armor})


# def equip_gear(request):
#     if request.method == 'POST':
#         character_id = request.POST.get('character_id')
#         gear_type = request.POST.get('gear_type')
#         selected_item_id = request.POST.get('selected_item')
#         character = Character.objects.get(id=character_id)
#         armor_model = get_armor_model(gear_type)
        
#         try:
#             selected_item = armor_model.objects.get(id=selected_item_id)
#         except armor_model.DoesNotExist:
#             return JsonResponse({'success': False, 'error': 'Выбранный предмет не найден'})
        
#         if gear_type == 'body':
#             character.equip_body_armor(selected_item)
#         elif gear_type == 'headArmor':
#             character.equip_head_armor(selected_item)
#         elif gear_type == 'bootsArmor':
#             character.equip_boots_armor(selected_item)
#         elif gear_type == 'glovesArmor':
#             character.equip_gloves_armor(selected_item)
#         elif gear_type == 'legsArmor':
#             character.equip_legs_armor(selected_item)
#         elif gear_type == 'backArmor':
#             character.equip_back_armor(selected_item)
#         elif gear_type == 'shoulderArmor':
#             character.equip_shoulder_armor(selected_item)
#         elif gear_type == 'wristArmor':
#             character.equip_wrist_armor(selected_item)
#         elif gear_type == 'beltArmor':
#             character.equip_belt_armor(selected_item)
#         elif gear_type == 'ringSlot1':
#             character.equip_ring1(selected_item)
#         elif gear_type == 'ringSlot2':
#             character.equip_ring2(selected_item)
#         elif gear_type == 'amulet':
#             character.equip_amulet(selected_item)
#         elif gear_type == 'trinketSlot1':
#             character.equip_trinket1(selected_item)
#         elif gear_type == 'trinketSlot2':
#             character.equip_trinket2(selected_item)
#         elif gear_type == 'weaponSlot1':
#             character.equip_weapon1(selected_item)
#         elif gear_type == 'weaponSlot2':
#             character.equip_weapon2(selected_item)

#         return JsonResponse({'success': True})

#     return JsonResponse({'success': False, 'error': 'Неверный запрос'})



def get_armor_model(gear_type):
    if gear_type == 'body':
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

def view_armors(request, armor_type , character_id):
    character = get_object_or_404(Character,  id=character_id)
    sort_by = request.GET.get('sort', 'level')  # Default to sorting by level
    order = request.GET.get('order', 'asc')  # Default to ascending order
    search_term = request.GET.get('search', '')

    if armor_type == 'body':
        armors = Body_armor.objects.all()
        template = 'body_armors.html'
    elif armor_type == 'head':
        armors = Head_armor.objects.all()
        template = 'head_armors.html'
    elif armor_type == 'boots':
        armors = Boots_armor.objects.all()
        template = 'boots_armors.html'
    elif armor_type == 'wirst':
        armors = Wrist_armor.objects.all()
        template = 'wirst_list.html'
    elif armor_type == 'gloves':
        armors = Gloves_armor.objects.all()
        template = 'gloves_armors.html'
    elif armor_type == 'legs':
        armors = Legs_armor.objects.all()
        template = 'legs_armors.html'
    elif armor_type == 'back':
        armors = Back_armor.objects.all()
        template = 'back_armors.html'
    elif armor_type == 'shoulder':
        armors = Shoulder_armor.objects.all()
        template = 'shoulder_armors.html'
    elif armor_type == 'belt':
        armors = Belt_armor.objects.all()
        template = 'belt_armors.html'
    elif armor_type == 'amulet':
        armors = Amulet.objects.all()
        template = 'amulet_list.html'
    elif armor_type == 'ring1':
        armors = Ring.objects.all()
        template = 'ring1_list.html'
    elif armor_type == 'ring2':
        armors = Ring.objects.all()
        template = 'ring2_list.html'
    elif armor_type == 'trinket1':
        armors = Trinket.objects.all()
        template = 'trinket1_list.html'
    elif armor_type == 'trinket2':
        armors = Trinket.objects.all()
        template = 'trinket2_list.html'
    elif armor_type == 'weapon':
        armors = Weapon.objects.all()
        template = 'weapon_list.html'

    if order == 'asc':
        sort_order = ''
    else:
        sort_order = '-'

    if sort_by == 'level':
        armors = armors.order_by(f'{sort_order}item_level')
    elif sort_by == 'name':
        armors = armors.order_by(f'{sort_order}title')


    if search_term:
        armors = armors.filter(title__icontains=search_term)

    next_order = 'desc' if order == 'asc' else 'asc'

    return render(request, template, {'armors': armors , 'armor_type':armor_type, 'character':character, 'order': next_order})

from django.urls import reverse

def equip_armor(request, character_id, armor_id, armor_type):
    character = get_object_or_404(Character, id=character_id)

    # Update the corresponding armor attribute based on the armor_type
    if armor_type == 'body_armor':
        armor_model = Body_armor
        character.body_armor = get_object_or_404(armor_model, id=armor_id)
    elif armor_type == 'head_armor':
        armor_model = Head_armor
        character.head_armor = get_object_or_404(armor_model, id=armor_id)
    elif armor_type == 'amulet':
        armor_model = Amulet
        character.amulet = get_object_or_404(armor_model, id=armor_id)
    elif armor_type == 'shoulder_armor':
        armor_model = Shoulder_armor
        character.shoulder_armor = get_object_or_404(armor_model, id=armor_id)
    elif armor_type == 'back_armor':
        armor_model = Back_armor
        character.back_armor = get_object_or_404(armor_model, id=armor_id)
    elif armor_type == 'wrist_armor':
        armor_model = Wrist_armor
        character.wrist_armor = get_object_or_404(armor_model, id=armor_id)
    elif armor_type == 'gloves_armor':
        armor_model = Gloves_armor
        character.gloves_armor = get_object_or_404(armor_model, id=armor_id)
    elif armor_type == 'belt':
        armor_model = Belt_armor
        character.belt_armor = get_object_or_404(armor_model, id=armor_id)
    elif armor_type == 'legs_armor':
        armor_model = Legs_armor
        character.legs_armor = get_object_or_404(armor_model, id=armor_id)
    elif armor_type == 'boots_armor':
        armor_model = Boots_armor
        character.boots_armor = get_object_or_404(armor_model, id=armor_id)
    elif armor_type == 'ring1':
        armor_model = Ring
        character.ring1 = get_object_or_404(armor_model, id=armor_id)
    elif armor_type == 'ring2':
        armor_model = Ring
        character.ring2 = get_object_or_404(armor_model, id=armor_id)
    elif armor_type == 'trinket1':
        armor_model = Trinket
        character.trinket1 = get_object_or_404(armor_model, id=armor_id)
    elif armor_type == 'trinket2':
        armor_model = Trinket
        character.trinket2 = get_object_or_404(armor_model, id=armor_id)
    elif armor_type == 'weapon':
        armor_model = Weapon
        character.weapon1 = get_object_or_404(armor_model, id=armor_id)    
    character.save()
    

    # Redirect the user back to the character profile page
    return HttpResponseRedirect(reverse('character_info', kwargs={'character_id': character_id}))


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

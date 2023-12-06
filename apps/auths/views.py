from django.shortcuts import render , redirect
from django.shortcuts import render, get_object_or_404
from .forms.login_form import LoginForm
from django.http.response import HttpResponse , HttpResponseRedirect , HttpResponseForbidden
from .forms.reg_form import RegistrationForm
from .forms.avatar_form import AvatarChangeForm
from django.contrib.auth import login, authenticate
from .models import Character
from wow_db.models import (Body_armor , Head_armor , Boots_armor ,
                           Gloves_armor , Legs_armor ,Back_armor,
                            Shoulder_armor , Wrist_armor , Belt_armor,
                            Ring , Trinket , Weapon , Amulet  )
from client_files.models import FileUploadForm
from news.forms.news_form import NewsCreationForm
from django.contrib.auth.decorators import login_required
from .forms.character_form import GameCharacterForm
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.urls import reverse
from django.contrib import messages

@login_required
def profile(request):
    user_account = request.user 
    characters = Character.objects.filter(user=request.user)

    if request.method == 'POST':
        avatar_form = AvatarChangeForm(request.POST, request.FILES, instance=request.user)
        if avatar_form.is_valid():
            avatar_form.save()

    avatar_form = AvatarChangeForm(instance=request.user)

    if request.user.is_staff:
        if request.method == 'POST':
            form = FileUploadForm(request.POST, request.FILES, user=request.user)
            if form.is_valid():
                uploaded_file = form.save(commit=False)
                uploaded_file.uploaded_by = request.user
                uploaded_file.save()
               
        else:
            form = FileUploadForm(user=request.user)
            
        if request.method == 'POST':
            news_form = NewsCreationForm(request.POST)
            if news_form.is_valid():
                news = news_form.save(commit=False)
                news.author = request.user
                news.save()
        else:
            news_form = NewsCreationForm()
        
        return render(request, 'profile.html', {'user_account': user_account, 'characters': characters,
                                                 'upload_form': form ,  'avatar_form': avatar_form ,'news_form':
                                                   news_form})

    return render(request, 'profile.html', {'user_account': user_account, 'characters': 
                                            characters ,  'avatar_form': avatar_form})


def character_info(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    character_class = character.specialization.class_armor_type.title
    
    body_armors = Body_armor.objects.all()
    head_armors = Head_armor.objects.all()
    boots_armors = Boots_armor.objects.all()
    gloves_armors = Gloves_armor.objects.all() 
    legs_armors = Legs_armor.objects.all()
    back_armors = Back_armor.objects.all()
    shoulder_armors = Shoulder_armor.objects.all()
    wrist_armors = Wrist_armor.objects.all()
    belt_armors = Belt_armor.objects.all() 
    amulet_armors = Amulet.objects.all()


    return render(request, 'character_info.html', {'character': character, 'body_armors': body_armors,
                                                   'head_armors': head_armors, 'boots_armors': boots_armors,
                                                   'gloves_armors': gloves_armors, 'legs_armors': legs_armors,
                                                   'back_armors': back_armors, 'shoulder_armors': shoulder_armors,
                                                   'wrist_armors': wrist_armors, 'belt_armors': belt_armors,
                                                   'amulet_armors': amulet_armors})



def view_armors(request, armor_type , character_id):
    character = get_object_or_404(Character,  id=character_id)
    sort_by = request.GET.get('sort', 'level')  
    order = request.GET.get('order', 'asc')  
    search_term = request.GET.get('search', '')
    game_class = character.specialization.class_armor_type.title
    class_weapons = character.specialization.class_weapon_type.all()
    weapon_types = [weapon_type for weapon_type in class_weapons]

    if armor_type == 'body':
        armors = Body_armor.objects.filter(armor_type=game_class)
        template = 'body_armors.html'
    elif armor_type == 'head':
        armors = Head_armor.objects.filter(armor_type=game_class)
        template = 'head_armors.html'
    elif armor_type == 'boots':
        armors = Boots_armor.objects.filter(armor_type=game_class)
        template = 'boots_armors.html'
    elif armor_type == 'wirst':
        armors = Wrist_armor.objects.filter(armor_type=game_class)
        template = 'wirst_list.html'
    elif armor_type == 'gloves':
        armors = Gloves_armor.objects.filter(armor_type=game_class)
        template = 'gloves_armors.html'
    elif armor_type == 'legs':
        armors = Legs_armor.objects.filter(armor_type=game_class)
        template = 'legs_armors.html'
    elif armor_type == 'back':
        armors = Back_armor.objects.all()
        template = 'back_armors.html'
    elif armor_type == 'shoulder':
        armors = Shoulder_armor.objects.filter(armor_type=game_class)
        template = 'shoulder_armors.html'
    elif armor_type == 'belt':
        armors = Belt_armor.objects.filter(armor_type=game_class)
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
        armors = Weapon.objects.filter(waepon_type__in=weapon_types)
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


def equip_armor(request, character_id, armor_id, armor_type):
    character = get_object_or_404(Character, id=character_id)
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
    
    return HttpResponseRedirect(reverse('character_info', kwargs={'character_id': character_id}))

from django.http import JsonResponse

def unequip_gear(request):
    if request.method == 'POST':
        character_id = request.POST.get('character_id')
        gear_type = request.POST.get('gear_type')
        character = Character.objects.get(id=character_id)

        if gear_type == 'bodyArmor':
            character.body_armor = None
        elif gear_type == 'headArmor':
            character.head_armor = None
        elif gear_type == 'amulet':
            character.amulet = None
        elif gear_type =='shoulder_armor':
            character.shoulder_armor = None
        elif gear_type == 'back_armor':
            character.back_armor = None
        elif gear_type == 'wrist_armor':
            character.wrist_armor = None
        elif gear_type == 'gloves_armor':
            character.gloves_armor = None
        elif gear_type == 'belt':
            character.belt_armor = None
        elif gear_type == 'legs_armor':
            character.legs_armor = None
        elif gear_type == 'boots_armor':
            character.boots_armor = None
        elif gear_type == 'ring1':
            character.ring1 = None
        elif gear_type == 'ring2':
            character.ring2 = None
        elif gear_type == 'trinket1':
            character.trinket1 = None
        elif gear_type == 'trinket2':
            character.trinket2 = None
        elif gear_type == 'weapon1':
            character.weapon1 = None
        elif gear_type == 'weapon2':
             character.weapon2 = None
        character.save()

    return JsonResponse({'status': 'error',})



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

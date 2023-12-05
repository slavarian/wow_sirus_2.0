from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import (Body_armor, Head_armor, Boots_armor,
                    Gloves_armor , Shoulder_armor , Belt_armor , 
                    Legs_armor ,Wrist_armor , Amulet , Ring , Back_armor ,
                     Trinket , Weapon )


def db_main_page(request):
    armor_type_filter = request.GET.get('armor_type', '')
    armor_slot_filter = request.GET.get('armor_slot', '')
    armor_quality_filter = request.GET.get('armor_quality', '')

    armor_model_slot = {
        'Грудь': Body_armor,
        'Голова': Head_armor,
        'Ступни': Boots_armor,
        'Кисти рук': Gloves_armor,
        'Плечи': Shoulder_armor,
        'Пояс': Belt_armor,
        'Ноги': Legs_armor,
        'Запястья': Wrist_armor,
        'Спина': Back_armor,
    }

    

    if armor_slot_filter in armor_model_slot:
        armor_model = armor_model_slot[armor_slot_filter]
        armors = armor_model.objects.all()
        search_term = request.GET.get('search', '')

        if armor_type_filter:
            armors = armors.filter(armor_type=armor_type_filter)

        if armor_quality_filter:
            armors = armors.filter(quality=armor_quality_filter)

        if search_term:
            armors = armors.filter(title__icontains=search_term)

        paginator = Paginator(armors, 25)
        page = request.GET.get('page')

        try:
            armors = paginator.page(page)
        except PageNotAnInteger:
            armors = paginator.page(1)
        except EmptyPage:
            armors = paginator.page(paginator.num_pages)

        context = {
            'armors': armors,
            'armor_type_filter': armor_type_filter,
            'armor_slot_filter': armor_slot_filter,
            'armor_quality_filter': armor_quality_filter,
            'search_term': search_term,
        }

        return render(request, 'db_main.html', context)
    else:
        return render(request, 'db_main.html', {})
    

def db_jewelry_page(request):
   
    armor_slot_filter = request.GET.get('jewelry_slot', '')
    armor_quality_filter = request.GET.get('jewelry_quality', '')

    jewelry_model_slot = { 
        'Шея': Amulet,
        'Палец': Ring,
        'Тринкет': Trinket,
    }

    

    if armor_slot_filter in jewelry_model_slot:
        armor_model = jewelry_model_slot[armor_slot_filter]
        armors = armor_model.objects.all()
        search_term = request.GET.get('search', '')

        if armor_quality_filter:
            armors = armors.filter(quality=armor_quality_filter)

        if search_term:
            armors = armors.filter(title__icontains=search_term)

        paginator = Paginator(armors, 25)
        page = request.GET.get('page')

        try:
            armors = paginator.page(page)
        except PageNotAnInteger:
            armors = paginator.page(1)
        except EmptyPage:
            armors = paginator.page(paginator.num_pages)

        context = {
            'armors': armors,
            'armor_slot_filter': armor_slot_filter,
            'armor_quality_filter': armor_quality_filter,
            'search_term': search_term,
        }

        return render(request, 'db_jewelry.html', context)
    else:
        return render(request, 'db_jewelry.html', {})
    

def db_weapon_page(request):
    weapon_type_filter = request.GET.get('weapon_type', '')
    weapon_quality_filter = request.GET.get('weapon_quality', '')

    
    weapons = Weapon.objects.all()
    search_term = request.GET.get('search', '')

    if weapon_type_filter:
        weapons = weapons.filter(waepon_type=weapon_type_filter)

    if  weapon_quality_filter:
        weapons = weapons.filter(quality=weapon_quality_filter)

    if search_term:
        weapons = weapons.filter(title__icontains=search_term)

    paginator = Paginator(weapons, 25)
    page = request.GET.get('page')

    try:
        weapons = paginator.page(page)
    except PageNotAnInteger:
        weapons = paginator.page(1)
    except EmptyPage:
        weapons = paginator.page(paginator.num_pages)

    context = {
            'weapons': weapons,
            'weapon_type_filter': weapon_type_filter,
            'weapon_quality_filter': weapon_quality_filter,
            'search_term': search_term,
        }

    return render(request, 'db_weapon.html', context)

    
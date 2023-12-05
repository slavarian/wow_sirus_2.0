from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Character
from wow_db.models import (Body_armor , Head_armor , Boots_armor ,
                           Gloves_armor , Legs_armor ,Back_armor,
                            Shoulder_armor , Wrist_armor , Belt_armor,
                            Ring , Trinket , Weapon , Amulet  )
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def character_raiting(request):
    characters = Character.objects.all()
    character_sorted = sorted(characters, key=lambda x: x.gear_score, reverse=True)
    paginator = Paginator(characters, 10)
    page = request.GET.get('page')

    try:
        characters = paginator.page(page)
    except PageNotAnInteger:
        characters = paginator.page(1)
    except EmptyPage:
        characters = paginator.page(paginator.num_pages)

    return render(request, 'character_raiting.html', {'character_sorted': character_sorted, 'characters': characters})


def character_views(request, character_id):
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
    return render(request, 'character_views.html', {'character': character, 'body_armors': body_armors ,
            'head_armors':head_armors,'boots_armor':boots_armor,'gloves_armor':gloves_armor,'back_armor':back_armor,
            'shoulder_armor':shoulder_armor,'belt_armor':belt_armor,'ring1':ring1,'trinket1':trinket1,'ring2':ring2,'trinket2':trinket2,
            'weapon1':weapon1,'weapon2':weapon2,'amulet':amulet,'wrist_armor':wrist_armor,'legs_armor':legs_armor})


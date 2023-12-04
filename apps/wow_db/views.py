from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import (Body_armor, Head_armor, Boots_armor,
                    Gloves_armor , Shoulder_armor , Belt_armor , 
                    Legs_armor ,Wrist_armor)


def db_main_page(request):
    armor_type_filter = request.GET.get('armor_type', '')
    armor_slot_filter = request.GET.get('armor_slot', '')

    armor_model_slot = {
        'Грудь': Body_armor,
        'Голова': Head_armor,
        'Ступни': Boots_armor,
        'Кисти рук': Gloves_armor,
        'Плечи': Shoulder_armor,
        'Пояс': Belt_armor,
        'Ноги': Legs_armor,
        'Запястья': Wrist_armor
    }

    

    if armor_slot_filter in armor_model_slot:
        armor_model = armor_model_slot[armor_slot_filter]
        armors = armor_model.objects.all()

        if armor_type_filter:
            armors = armors.filter(armor_type=armor_type_filter)

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
        }

        return render(request, 'db_main.html', context)
    else:
        return render(request, 'db_main.html', {})
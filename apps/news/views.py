from django.shortcuts import render
from .models import News

def news_page(request):
    news_list = News.objects.all().order_by('-date_create')
    return render(request, 'news_page.html', {'news_list': news_list})
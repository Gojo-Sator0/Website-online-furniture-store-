from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#main page
def index(request):
    context = {
        'title':'HOME - Главная',
        'content':'Магазин мебели HOME'
  
    }

    return render(request, template_name='main/index.html', context=context)

def about(request):
    context = {
        'title':'HOME - О нас',
        'content':'О нас',
        'text_on_page':'Текст и описания магазина'
  
    }

    return render(request, template_name='main/about.html', context=context)


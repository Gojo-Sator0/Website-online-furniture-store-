from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#main page
def index(request):
    context = {
        'title':'Home',
        'content':'Главная страница магазина - Home',
        'list':['first', 'second'],
        'dict':{'first':1},
        'is_authentication': True    
    }

    return render(request, template_name='main/index.html', context=context)

def about(request):
    return HttpResponse('Home page is about')

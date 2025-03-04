from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.urls import reverse

from orders.models import Order, Orderitem
from carts.models import Cart
from users.forms import UserLoginForm, UserProfileForm, UserRegisterForm
from django.db.models import Prefetch


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{user.username}, Вы успешно вошли в систему")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)
                    

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:login'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()


    context={
        'title':'HOME - Авторизация',
        'form':form,
    }
    return render(request,'users/login.html',context)

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            messages.success(request, f"{user.username}, Вы успешно зарегистрировались")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()

    context={
        'title':'HOME - Регистрация',
        'form':form,
    }
    return render(request,'users/registration.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно обновлены')
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    orders = ( 
        Order.objects.filter(user=request.user)
            .prefetch_related(
                Prefetch(
                    'orderitem_set', 
                    queryset=Orderitem.objects.select_related('product')
                    )
            )
            .order_by('-id')
    )
                            

    context={
        'title':'HOME - Кабинет',
        'form':form,
        'orders':orders,
    }
    return render(request,'users/profile.html',context)

def users_cart(request):
    context={
        'title':'HOME - Корзина',
    }
    return render(request,'users/users_cart.html',context)

@login_required
def logout(request):
    messages.success(request, 'Вы успешно вышли из системы')
    auth.logout(request)
    return redirect(reverse('main:index'))
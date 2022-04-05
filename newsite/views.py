from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from .cart import Cart
from .models import Service, Order, OrderStatus
from .forms import UserRegForm, UserLogForm
import datetime


def main(request):
    services_photo = []
    services_count = 0
    if request.user.is_authenticated:
        flag = True
    else:
        flag = False
    services = Service.objects.filter(service_is_active=True)
    for i in services:
        services_photo.append(i.service_photo)
    cart = Cart(request.session)
    for i in cart.view_service().keys():
        services_count += cart.view_service().get(i)
    return render(request, 'newsite/main.html', {'flag': flag, 'cart': cart.view_service(), 'services': services, 'services_photo': services_photo, 'services_count': services_count})


def contacts(request):
    services_count = 0
    if request.user.is_authenticated:
        flag = True
    else:
        flag = False
    cart = Cart(request.session)
    for i in cart.view_service().keys():
        services_count += cart.view_service().get(i)
    return render(request, 'newsite/contacts.html', {'flag': flag, 'cart': cart.view_service(), 'services_count': services_count})


def login_page(request):
    services_count = 0
    cart = Cart(request.session)
    for i in cart.view_service().keys():
        services_count += cart.view_service().get(i)
    if request.method == "POST":
        form = UserLogForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect(('/'), pk=user.pk)
            else:
                return render(request, 'newsite/error_login_page.html', {'form': form, 'services_count': services_count})
        else:
            print(form.errors)
    else:
        form = UserLogForm()
        return render(request, 'newsite/login_page.html', {'form': form, 'services_count': services_count})


def reg_page(request):
    services_count = 0
    cart = Cart(request.session)
    for i in cart.view_service().keys():
        services_count += cart.view_service().get(i)
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'],
                                            email=form.cleaned_data['email'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'],)
            return redirect(('/login_page'), pk=user.pk)
    else:
        form = UserRegForm()
    return render(request, 'newsite/reg_page.html', {'form': form, 'services_count': services_count})


def logout_page(request):
    services_count = 0
    cart = Cart(request.session)
    for i in cart.view_service().keys():
        services_count += cart.view_service().get(i)
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'newsite/logout_page.html', {'services_count': services_count})
    else:
        return redirect('/login_page')


def add_service(request, service_id, project_id):
    cart = Cart(request.session)
    cart.add_service(service_id)
    if project_id == 1:
        return redirect(to='/', name='main')
    if project_id == 2:
        return redirect('/cart')


def del_service(request, service_id):
    cart = Cart(request.session)
    cart.del_service(service_id)
    return redirect('/cart')


def cart(request):
    services_count = 0
    cart = Cart(request.session)
    cost = cart.total_cost()
    finally_dict = {}
    for i in cart.view_service():
        services = []
        services.append(i)
        service = Service.objects.get(pk=i)
        services.append(service.service_name)
        services.append(service.service_price)
        services.append(cart.view_service().get(i))
        finally_dict[str(i)] = services
    if request.user.is_authenticated:
        flag = True
    else:
        flag = False
    for i in cart.view_service():
        services_count += cart.view_service().get(i)
    return render(request, 'newsite/cart.html', {'flag': flag, 'cart': cart.view_service(), 'services_count': services_count, 'cost': cost, 'finally_dict': finally_dict})


def profile(request):
    history = Order.objects.filter(user=request.user)
    if len(history) == 0:
        history = 0
    services_count = 0
    cart = Cart(request.session)
    for i in cart.view_service().keys():
        services_count += cart.view_service().get(i)
    return render(request, 'newsite/profile.html', {'cart': cart.view_service(), 'services_count': services_count, 'history': history})


def create_order(request):
    services_count = 0
    cart = Cart(request.session)
    for i in cart.view_service().keys():
        services_count += cart.view_service().get(i)
    services = []
    for i in cart.view_service().keys():
        services.append(('Услуга: %s(id = %s), количество %s') % (
            Service.objects.get(id=i).service_name, i, cart.view_service().get(i)))
    Order.objects.create(
        user=request.user,
        services='\n'.join(services),
        cost=int(cart.total_cost()),
        user_text='Примечание отсутствует',
        status=OrderStatus.objects.get(pk='2'),
        date=datetime.datetime.now()
    )
    cart.del_all_service()
    return redirect('/cart')

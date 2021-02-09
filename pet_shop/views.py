from django.contrib import messages
from django.shortcuts import render, redirect
from pet_shop.models import Order
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout



def index(request):
    orders = Order.objects.all()
    return render(request, "pet_shop/index.html", {"order_list": orders})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "username or password is incorrect")
        return render(request, "pet_shop/login.html")



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

        return render(request, "pet_shop/register.html", {"form": form})



def logoutUser(request):
    logout(request)
    return redirect('login')


def createOrder(request):
    context = {}
    return render(request, 'pet_shop/order_form.html', context)

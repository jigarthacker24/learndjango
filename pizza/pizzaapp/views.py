from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PizzaModel

# Create your views here.

def adminloginview(request):
    return render(request,"pizzaapp/adminlogin.html")

def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    #user exist
    if user is not None and user.username == 'admin':
        login(request, user)
        return redirect('adminhomepage')

    #user doesnt exist
    if user is None:
        messages.add_message(request, messages.ERROR,'Invalid credentials')
        return redirect('adminloginpage')

def adminhomepageview(request):
    context = {'pizza': PizzaModel.objects.all()}
    return render(request,"pizzaapp/adminhomepage.html",context)

def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')

def addpizza(request):
    name = request.POST['pizza']
    price = request.POST['price']

    # add values to database

    PizzaModel(name=name, price=price).save()

    return redirect('adminhomepage')

def deletepizza(request, pizzapk):
    PizzaModel.objects.filter(id=pizzapk).delete()
    return redirect('adminhomepage')

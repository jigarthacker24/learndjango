from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PizzaModel, CustomerModel,OrderModel
from django.contrib.auth.models import User

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

def homepageview(request):
    return render(request,'pizzaapp/homepage.html')

def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneno = request.POST['phone']

    #if username already exist
    if User.objects.filter(username=username).exists():
        messages.add_message(request,messages.ERROR,"User already present")
        return redirect('homepage')
    #if username is not present, create new user
    User.objects.create_user(username=username,password=password).save()
    new_user = User.objects.filter(username=username)[0]
    CustomerModel(userid = new_user.id,phoneno=phoneno).save()
    messages.add_message(request,messages.INFO,"User created successfully")
    return redirect('homepage')

def userloginview(request):
    return render(request,"pizzaapp/userlogin.html")

def userauthenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    #user exist
    if user is not None:
        login(request, user)
        return redirect('customerpage')

    #user doesnt exist
    if user is None:
        messages.add_message(request, messages.ERROR,'Invalid credentials')
        return redirect('userloginpage')

def customerpageview(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')
    username = request.user.username
    context = {'name':username, 'pizzas':PizzaModel.objects.all()}
    return render(request,'pizzaapp/customerwelcome.html',context)

def logoutuser(request):
    logout(request)
    return redirect('userloginpage')

def placeorder(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')
    username=request.user.username
    phoneno=CustomerModel.objects.filter(userid=request.user.id)[0].phoneno
    address=request.POST['address']
    ordereditems=""

    for pizza in PizzaModel.objects.all():
        pizzaid = pizza.id
        pizzaname = pizza.name
        pizzaprice = pizza.price
        pizzaqty = str(request.POST.get(str(pizzaid),0))
        if pizzaqty != "0":
            ordereditems = ordereditems + pizzaname + " " + str(int(pizzaprice)*int(pizzaqty)) + " " + pizzaqty + ";"


    OrderModel(username=username,phoneno=phoneno,address=address,ordereditems=ordereditems).save()
    messages.add_message(request,messages.INFO,"Order placed successfully.")
    return redirect('customerpage')


def userorders(request):
    context = {'orders': OrderModel.objects.filter(username=request.user.username)}
    return render(request,'pizzaapp/userorders.html',context)

def adminorders(request):
    orders = OrderModel.objects.all()
    context = {'orders':orders}
    return render(request,'pizzaapp/adminorders.html',context)

def acceptorder(request,orderpk):
    order = OrderModel.objects.filter(id=orderpk)[0]
    order.status = "accepted"
    order.save()
    return redirect(request.META['HTTP_REFERER'])

def declineorder(request,orderpk):
    order = OrderModel.objects.filter(id=orderpk)[0]
    order.status = "declined"
    order.save()
    return redirect(request.META['HTTP_REFERER'])

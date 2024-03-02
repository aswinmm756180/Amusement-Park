from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import UserAddForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from staff_app.models import Foodlist
from .models import Bookticket
from.models import *


# Create your views here.
def index(request):
    return render(request,"index.html")

def signup(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            user = form.save()  
            group = Group.objects.get(name='users')  
            user.groups.add(group)  
            messages.info(request, "User Created")
            return redirect('signin')
        else:
            messages.error(request, "Form validation failed.Try passwords using letters symbols and numbers(8 atleast),don't use passwords  similar to username.")
            print("Form errors:", form.errors)
    else:
        form = UserAddForm()
    return render(request, "signup.html", {"form": form})

def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request .session["username"]=username
            request .session["password"]=password
            login(request,user)
            return redirect("viewpage")
        else:
            
            messages.info(request,"Username or Password Incorrect")
            return redirect("signin")

    return render(request,"signin.html")


def signout(request):
    logout(request)
    return redirect("signin")  

def viewpage(request):
    return render(request,"viewpage.html")


def view_food(request):
    food=Foodlist.objects.all().order_by("-food_id")
    return render(request,"viewfood.html",{"all_food":food})


def book_ticket(request):
    if request.method == 'POST':
        name1=request.POST.get('name') 
        age1=request.POST.get('age')
        phno1=request.POST.get('phno')
        book=Bookticket.objects.create(
            name=name1,
            age=age1,
            phone=phno1,

        )
        book.save()
        messages.success(request,'TICKET BOOKED SUCCESSFULLY')
    return render(request,'ticketbook.html')



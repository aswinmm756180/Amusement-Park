from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import UserAddForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from staff_app.models import Foodlist

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

def viewpage(request):
    return render(request,"viewpage.html")


def view_food(request):
    food=Foodlist.objects.all().order_by("-food_id")
    return render(request,"viewfood.html",{"all_food":food})






def book_room(request):
    if request.method == 'POST':
        user = request.user
        room = request.POST.get('room')
        bed = str(request.POST.get('bed'))  # Convert to string
        date_str = request.POST.get('date')  # Assuming you have a separate date input
        date = timezone.make_aware(datetime.strptime(date_str, '%Y-%m-%d'))
        current_time = timezone.now()

        # Check if the room is already full
        if Booking.objects.filter(room=room, date=date).count() >= 5:
            messages.info(request, "The room is full")
        
        # Check if the requested bed in the room is already booked
        if Booking.objects.filter(room=room, bed=bed, date=date).exists():
            messages.info(request, "The bed is already booked")  
        
        # Create a new booking with current time
        booking = Booking.objects.create(user=user, room=room, bed=bed, time=current_time, date=date)
        booking.save()
        
        return redirect('booking_confirmation', booking_id=booking.id)  # Redirect with booking ID
    
    return render(request, 'booking.html', {'rooms_choice': Booking.rooms_choice, 'beds_choice': Booking.beds_choice})



#     @login_required
# def booking_confirmation(request):
#     user = request.user
#     booking = Booking.objects.filter(user=user).first()
#     return render(request, 'booking_details.html', {'booking': booking})
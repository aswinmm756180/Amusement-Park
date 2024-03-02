from django.shortcuts import render,redirect
from .forms import FoodDetailsForm
from .models import Foodlist
from .models import staff
from django.contrib import messages
# from django.contrib.auth import authenticate,logout,login as auth-login
# from django.contrib.auth.models import staff

# Create your views here.






def viewusers(request):
    users = User.objects.all()
    return render(request, "staff/viewuser.html", {"users": users})


    
def Food_list(request):
    food=Foodlist.objects.all().order_by("-food_id")
    return render(request,"staff/view_food_list.html",{"all_food":food})

def add_food(request):
    Food_categories = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    )
    form = FoodDetailsForm()
    
    if request.method == 'POST':
        form = FoodDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Successfully added to the food menu")
            return redirect('Food_list')
        else:
            form = FoodDetailsForm()

    return render(request, "staff/add_food.html", {'form': form, 'Food_categories': Food_categories})
   


from django.shortcuts import render, get_object_or_404, redirect
from .models import Foodlist
from .forms import FoodDetailsForm



def edit_food(request, food_id):
    food = get_object_or_404(Foodlist, food_id=food_id)

    if request.method == 'POST':
        form = FoodDetailsForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('Food_list')
    else:
        form = FoodDetailsForm(instance=food)

    return render(request, 'staff/edit_food.html', {'form': form, 'food': food})


def deletefood(request,pk):
    edit=Foodlist.objects.get(food_id=pk)
    edit.delete()
    messages.info(request,"deleted")
    return redirect("Food_list")



from django.contrib.auth.decorators import login_required
@login_required
def admin_dashboard(request):
    pending_bookings = Booking.objects.filter(approved=False)
    return render(request, 'staff/dashboard.html', {'pending_bookings': pending_bookings})


def staff_register(request):
    if request.method=='POST':
        staffname=request.POST.get('name')
        staffusername=request.POST.get('username')
        staffemail=request.POST.get('email')
        staffpassword=request.POST.get('pass')
        staffuser=staff.objects.create_user(
            staffname=sname,
            staffusername=susernanme,
            staffemail=semail,
            staffpassword=spassword,
        )
        staffuser.save()
        messages.success(request,'SUCCESSFULLY REGISTER')
        # return redirect('login')
    return render(request,'staffsignup.html')
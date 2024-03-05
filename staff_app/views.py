from django.shortcuts import render,redirect
from .forms import FoodDetailsForm
from .models import Foodlist
from .models import staff
from django.contrib import messages
from .forms import StaffRegistrationForm







from django.shortcuts import render, redirect
# from .forms import StaffRegistrationForm

def staff_register(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            staff = form.save(commit=False)

            # Check if passwords match
            if staff.password == staff.password2:
                staff.save()
                return redirect('staff_login')  # Redirect to a success page
            else:
                form.add_error('password2', 'Passwords do not match.')
    else:
        form = StaffRegistrationForm()

    return render(request, 'staff/staffsignup.html', {'form': form})




from django.contrib.auth import authenticate, login
from .forms import StaffLoginForm




def staff_login(request):
    if request.method == 'POST':
        form = StaffLoginForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, usernanme=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('manage_staff')  # Redirect to a success page
            else:
                form.add_error(None,'Invalid username or password.')
                return redirect('staff_login') 

    else:
        form = StaffLoginForm()

    return render(request,'staff/stafflogin.html', {'form': form})



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


def manage_staff(request):
    return render(request,'staff/staffmanage.html')





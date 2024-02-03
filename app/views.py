from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from .forms import SignupForm,FoodDonationForm,OrderForm,Loginform
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib import messages
from .models import FoodDonation,FoodItem,Order

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        #form = SignupForm(request.POST)
        #if form.is_valid():
           # form.save()
        user=User(username=username,password=password,email=email)
        user.save()
        return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form=Loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password =password)
            if user is not None:
                login(request,user)
                try:
                    user_profile = UserProfile.objects.get(user=user)
                    user_type = user_profile.usertype
                    if user_type == 'volunteer':
                        return redirect('deliverlogin/')
                    elif user_type == 'ngo':
                        return redirect('post/')  
                    elif user_type == 'donor':

                        return redirect('donate') 
                    else:
                        messages.error(request, 'Invalid user type')
                except UserProfile.DoesNotExist:
                    messages.error(request, 'User profile not found')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Credentials Invalid')
    else:
        form = Loginform()
    return render(request, 'login.html', {'form': form})
def food_donation_form(request):
    if request.method == 'POST':
        form = FoodDonationForm(request.POST)
        if form.is_valid():
            foodname=request.POST['foodname']
            email=request.POST['email']
            phoneno=request.POST['phoneno']
            quantity=request.POST['quantity']
            address=request.POST['address']
            form.save()
            return redirect('donate/')  # Redirect to a thank-you page or another page
    else:
        form = FoodDonationForm()

    return render(request, 'donate.html', {'form': form})

def home(request):
    return render(request,'homepage.html')

def dashboard(request):
    # Fetch relevant data for the dashboard
    total_donations = FoodDonation.objects.count()
    total_food_items = FoodItem.objects.count()
    total_users = User.objects.count() 
    food_items = FoodDonation.objects.all()
    context = {
        'total_donations': total_donations,
        'total_food_items': total_food_items,
        'total_users':total_users,
        'food_items':food_items,

        #'total_volunteers': total_volunteers,
    }

    return render(request, 'dashboard.html', context)

def post(request):
    return render(request,'post.html')

def order_page(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user  # Assign the current user as the customer
            order.save()
            return redirect('order.html')
              # Redirect to a success page after order submission
    else:
        form = OrderForm()

    return render(request, 'order.html', {'form': form})

def donatesuccess(request):
    return render(request,'donatesuccess.html')

def food_items(request):
    
    food_items = FoodDonation.objects.all()
    return render(request, 'post.html', {'food_items': food_items})

def delivery(request):
    food_items = FoodDonation.objects.all()
    all_orders = Order.objects.all()
    return render(request, 'deliverlogin.html', {'all_orders': all_orders, 'food_items': food_items})

def accept_order(request):
    return render(request,'accept_order.html')

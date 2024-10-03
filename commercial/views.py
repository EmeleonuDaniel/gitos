from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import messages
from .models import Products
from django.contrib.auth.decorators import login_required
from .models import VendorProfile
from datetime import datetime
from .forms import VendorProfileForm
from .models import UserProfile
from .forms import UserProfileForm

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    products = Products.objects.all()
    return render(request, 'shop.html', {'products': products})

def testimonial(request):
    return render(request, 'testimonial.html')

def why(request):
    return render(request, 'why.html')

def login(request):
        if request.method == 'POST':
            username_or_email = request.POST.get('username_or_email',default=None)
            password = request.POST['password']
            user = authenticate(username=username_or_email,password=password)

            if user is None:
                #if username didn't work try authenticating with email
                try:
                    #find the user using email
                    user_with_email = User.objects.get(email=username_or_email)
                    user = authenticate(request ,username = user_with_email.username, password=password)
                except User.DoesNotExist:
                    user = None

            if user is not None:
                auth_login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Invalid credentials')
                return redirect('login')
        else:
            return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', default=None)
        email = request.POST.get('email', default=None)
        password = request.POST['password']
        passwordConfirmed = request.POST['passwordConfirmed']

        if password == passwordConfirmed:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already registered with Giftos maybe you would want to Login')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

def manage(request):
    return render(request, 'manage.html')

@login_required
def register(request):
    if request.method == 'POST':
        user = request.user #retrieve currently logged user
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()#strip is only used as a safety precaution method to remove all whitespaces from the beginning and end of the string 
        dob_str = request.POST.get('DOB', '').strip()
        gender = request.POST.get('gender', '').strip()
        address = request.POST.get('address', '').strip()
        phone = request.POST.get('phone', '').strip()
        package = request.POST.get('package', '').strip()
        
        if not first_name and last_name:
            return render(request, 'register.html', {'error': 'First name nad last name are required'})

        dob = None
        if dob_str:
            try:
                dob = datetime.strptime(dob_str, '%d/%m/%Y').date() #convert DD/MM/YYYY to YYYY/MM/DD
            except ValueError:
                return render(request, 'register.html', {'error': 'Invalid date format. use dd/mm/yyyy'})

        # Get or create the user profile record
        profile, _ = VendorProfile.objects.get_or_create(user=user)
        profile.first_name = first_name
        profile.last_name = last_name
        profile.DOB = dob
        profile.gender = gender
        profile.address = address
        profile.phone = phone
        profile.package = package
        profile.save()

        sellers_group = Group.objects.get(name='sellers')
        sellers_group.user_set.add(user)

        return redirect('profile_success')  # Redirect to a success page or profile page

    return render(request,'register.html')#come back later when you have a seller dashboard


    
def user_profile(request):
    return render(request, 'user_profile.html')

'''@login_required
def vendor_profile_setup(request,seller_id):
    #Get the existing seller profile based on the seller id
    seller_profile = get_object_or_404(VenProfile, id=seller_id)
    #check if vendor profile for the seller profile already exists
    try:
        vendor_profile = VendorProfile.objects.get(seller_profile=seller_profile,user=user)
    except VendorProfile.DoesNotExist:
        vendor_profile = None
    if request.method == 'POST':
        form = VendorProfileForm(request.POST, request.FILES, instance=vendor_profile)
        user = request.user
        brand_name = request.POST.get('BrandName', '').strip()
        WA_link = request.POST.get('url', '')
        
        profile, _ = VendorProfile.objects.get_or_create(user=user)

        profile.brand_name = brand_name
        profile.WA_link = WA_link
        
        if form.is_valid():
            #Link the new vendor profile with the existing Seller profile
            vendor_profile = form.save(commit=False)
            vendor_profile.seller_profile = seller_profile
            vendor_profile.save()

        return redirect('vendor_profile')
    
    return render(request, 'vendor_profile_setup.html')'''

def vendor_profile(request):
    return render(request, 'vendor_profile.html')

@login_required
def contact_details(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            # Update the manual fields after form.save()
            user = request.user
            first_name = request.POST.get('first_name','').strip()
            last_name = request.POST.get('last_name','').strip()
            location = request.POST.get('location','').strip()

            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.first_name = first_name
            profile.last_name = last_name
            profile.location = location
            profile.save()

            return redirect('user_profile')
        else:
            form = UserProfileForm(instance=request.user.userprofile)
            return render(request, 'contact-details.html', {'form': form})

    return render(request, 'contact-details.html')
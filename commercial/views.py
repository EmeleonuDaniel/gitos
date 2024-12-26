from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import messages
from .models import Products,Product,UserProfile,VendorProfile
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import VendorProfileForm,UserProfileForm

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    product_list = Product.objects.all()
    products = Products.objects.all()
    return render(request, 'shop.html', {'products': products, 'product_list': product_list})

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
        user = request.user 
        vendorprofile,created = VendorProfile.objects.get_or_create(user=user)
        form = VendorProfileForm(request.POST, request.FILES, instance=request.user.vendorprofile)
        if form.is_valid():
            form.save()
            
            store_name = request.POST.get('store_name', '').strip()
            WA_link = request.POST.get('url', '').strip()
            dob_str = request.POST.get('DOB', '').strip()
            gender = request.POST.get('gender', '').strip()
            store_address = request.POST.get('address', '').strip()
            phone = request.POST.get('phone', '').strip()
            package = request.POST.get('package', '').strip()

            dob = None
            if dob_str:
                try:
                    dob = datetime.strptime(dob_str, '%d/%m/%Y').date() #convert DD/MM/YYYY to YYYY/MM/DD
                except ValueError:
                    return render(request, 'register.html', {'error': 'Invalid date format. use dd/mm/yyyy'})

            profile = form.instance
            profile.brand_name = store_name
            profile.WA_link = WA_link
            profile.DOB = dob
            profile.gender = gender
            profile.address = store_address
            profile.phone = phone
            profile.package = package
            profile.save()

            vendors_group = Group.objects.get(name='vendors')
            vendors_group.user_set.add(user)

            return redirect('vendor_profile')
        else:
            print(form.errors)
    else:
        user = request.user
        vendorprofile,created = VendorProfile.objects.get_or_create(user=user)
        form = VendorProfileForm(instance=request.user.vendorprofile)
    return render(request,'register.html')

def user_profile(request):
    return render(request, 'user_profile.html')

def vendor_profile(request):
    
    return render(request, 'vendor_profile.html')

@login_required
def contact_details(request):
    if request.method == 'POST':
        user = request.user
        userprofile, created = UserProfile.objects.get_or_create(user=user)
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            # Update the manual fields after form.save()
            
            first_name = request.POST.get('first_name','').strip()
            last_name = request.POST.get('last_name','').strip()
            location = request.POST.get('location','').strip()
            email = request.POST.get('email', '').strip()

            profile = form.instance
            profile.first_name = first_name
            profile.last_name = last_name
            profile.location = location
            profile.email = email
            profile.save()

            return redirect('user_profile')
        else:
            print(form.errors)
    else:
        user = request.user
        userprofile, created = UserProfile.objects.get_or_create(user=user)
        form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'contact-details.html')

def vendor_profile(request):
    
    return render(request, 'vendor profile.html')

def vendor_details(request):
    if request.method == 'POST':
        user = request.user
        vendorprofile, created = VendorProfile.objects.get_or_create(user=user)
        form = VendorProfileForm(request.POST, request.FILES, instance=request.user.vendorprofile)
        if form.is_valid():
            form.save()

            brand_name = request.POST.get('brand_name','').strip()
            address = request.POST.get('address','').strip()
            phone = request.POST.get('phone','').strip()
            WA_link = request.POST.get('WA_link','').strip()

            profile = form.instance
            profile.brand_name = brand_name
            profile.address = address
            profile.phone = phone
            profile.WA_link = WA_link
            profile.save()
            return redirect('vendor_profile')
        else:
            print(form.errors)
    else:
        form = VendorProfileForm(instance=request.user.vendorprofile)    
        return render(request, 'vendor details.html')

@login_required
def sell_product(request):
    if request.method == 'POST':
            name = request.POST.get('name','').strip()
            description = request.POST.get('description','').strip()
            price = request.POST.get('price','').strip()
            stock = request.POST.get('stock','').strip()
            category = request.POST.get('category','').strip()
            product = Product.objects.create(vendor=request.user.vendorprofile,name=name, description=description, price=price, stock=stock, category=category)

            product.image1 = request.FILES.get('image1')
            product.image2 = request.FILES.get('image2')
            product.image3 = request.FILES.get('image3')
            product.image4 = request.FILES.get('image4')
            product.image5 = request.FILES.get('image5')
            product.image6 = request.FILES.get('image6')
            product.save()
        
            return redirect('product_list')
    else:       
        return render(request, 'sell-product.html')

def product_list(request):
    product_list = Product.objects.filter(vendor=request.user.vendorprofile)
    return render(request, 'product list.html',{'products': product_list,})

def product_page(request, pk):
    product =  get_object_or_404(Product, pk=pk)
    return render(request, 'product page.html')
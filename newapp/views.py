from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from newapp import models
# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def admin_dashboard(request):
    if not request.session.get('admin_logged_in'):
        return redirect('admin_login')
    return render(request, 'admin_dashboard.html')  # your dashboard page

def registration(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        password=request.POST.get('password')
        image=request.FILES.get('image')
        if models.Register.objects.filter(email=email).exists():
            alert="<script>alert('email alredy exist');windo.location.href='/registration/';</script>"
            return HttpResponse(alert)
        else :
            user=models.Register(name=name,age=age,email=email,image=image,password=password)
            user.save()
            return redirect('login')
    else :
        return render(request,'registration.html') 
def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        if models.Register.objects.filter(email=email,password=password).exists():
            request.session['email']=email
            return redirect('home')
        else:
            return redirect('home')
            
    else:
        return render(request,'login.html')

def profile(request):
    if 'email' in request.session: 
        email=request.session['email']
        user=models.Register.objects.get(email=email)
        return render(request,'profile.html',{'user':user})
    return render(request,'login.html')

def edit_profile(request):
    email=request.session['email']
    print(email)
    user=models.Register.objects.get(email=email)
    if request.method=='POST':
        user.name=request.POST.get('name')  
        user.age=request.POST.get('age')
        user.email=request.POST.get('email')
        user.password=request.POST.get('password')
        user.save()
        alert="<script>alert('profile edited succesfully');window.location.href='/profile/';</script>"
        return HttpResponse(alert)
    return render(request,'edit_profile.html',{'user':user})




from django.shortcuts import render
from .models import Product

def product_register(request):
    if request.method == 'POST':
        product_category = request.POST.get('category')
        product_name = request.POST.get('name')
        product_brand = request.POST.get('brand')
        product_image = request.FILES.get('image')
        product_price = request.POST.get('price')
        product_discound = request.POST.get('discound')
        product_description = request.POST.get('description')
        product_stock = request.POST.get('stock')
        product_IsAvailable = request.POST.get('is_available') == 'on'

        user = Product(
            product_category=product_category,
            product_name=product_name,
            product_brand=product_brand,
            product_image=product_image,
            product_price=product_price,
            product_discound=product_discound,
            product_description=product_description,
            product_stock=product_stock,
            product_IsAvailable=product_IsAvailable
        )
        user.save()
        return redirect('home')
    return render(request, 'product_register.html')


def delete(request,id):
    user=models.Register.objects.get(id=id).delete()
    return redirect(request,'index.html')


def product_list(request):
    products=models.Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def edit_product(request,id):
    product=models.Product.objects.get(id=id)
    if request.method == 'POST':
        product.product_category = request.POST.get('category')
        product.product_name = request.POST.get('name')
        product.product_brand = request.POST.get('brand')
        product.product_image = request.FILES.get('image')
        product.product_price = request.POST.get('price')
        product.product_discound = request.POST.get('discound')
        product.product_description = request.POST.get('description')
        product.product_stock = request.POST.get('stock')
        product.product_IsAvailable = request.POST.get('is_available') == 'on'
        product.save()
        return redirect('admin_product_list')
    return render(request,'edit_product.html',{'product':product})

def delete_product(request,id):
    user=models.Product.objects.get(id=id).delete()
    return redirect('admin_product_list')


def admin_product_list(request):
    products=models.Product.objects.all()
    return render(request, 'admin_product_list.html', {'products': products})
from django.shortcuts import render, redirect
from django.contrib import messages

def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email == 'admin' and password == 'admin':
            request.session['admin_logged_in'] = True
            return redirect('admin_dashboard')  # Replace with your actual dashboard URL name
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'admin_login.html')


def registor_list(request):
    registor=models.Register.objects.all()
    return render(request, 'registor_list.html', {'Register': registor})


def delete_registor(request,id):
    registor=models.Register.objects.get(id=id).delete()
    return redirect('registor_list')

def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    email=request.session['email']
    user=models.Register.objects.get(email=email)
    print(user)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        userd = models.Register.objects.get(email=email) 

        # Calculate total price
        discounted_price = product.product_price - product.product_discound
        total_price = discounted_price * quantity

        # Save to cart
        models.Cart.objects.create(
            user=user,
            product=product,
            quantity=quantity,
            total_price=total_price
        )
        return redirect('home')

    return render(request, 'cart_quantity.html', {'product': product})

def cart_list(request):
    email=request.session['email']
    user=models.Register.objects.get(email=email)
    
    carts=models.Cart.objects.filter(user=user)
    
    return render(request,'cart_list.html',{'carts':carts})




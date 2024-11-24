from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import user_item, Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid login credentials.')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password_r = request.POST['password_r']
        if password==password_r:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered.')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=fname,
                    last_name=lname,
                    email=email,
                    password=password
                )
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match.')
            return redirect('register')
    else:
        return render(request, 'register.html')
    
def wardrobe(request):
    items = user_item.objects.filter(user=request.user)
    return render(request, 'wardrobe.html', {'items': items})

def wardrobe_items(request, name):
    items = user_item.objects.filter(user=request.user).filter(category=name)
    return render(request, 'wardrobe_items.html', {'items': items, 'name': name})

def delete(request,item_id): 
    item = get_object_or_404(user_item, id=item_id)
    if request.method=='POST':
        item.delete() 
        previous_page = request.META.get('HTTP_REFERER')
        if previous_page:
            return redirect(previous_page)  # Reload the previous page
        else:
            return redirect('default-view')
    return redirect('/wardrobe')

def add(request):
    if request.method=='POST':
        category = request.POST['category']
        brand = request.POST['brand']
        color = request.POST['color']
        type = request.POST['type']
        size = request.POST['size']
        image = request.FILES.get('image')
        uio = user_item.objects.create(
            user = request.user,
            banner=image,
            category=category,
            brand=brand,
            color=color,
            type=type,
            size=size
        )
        uio.save()
        return redirect('/wardrobe')
    return render(request, 'add-item.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        co = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        return redirect('/')
    return render(request, 'contact.html')
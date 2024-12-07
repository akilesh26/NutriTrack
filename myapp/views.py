from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Food, Contact
from .forms import UploadFileForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def predict(image):
    #pass the image to model
    #this prediction is a place holder
    
    prediction = {
        "food": "Grilled Chicken Salad",
        "serving_size": "1 bowl",
        "calories": "350",
        "carbohydrates": "20g",
        "protein": "30g",
        "fat": "15g",
        "fiber": "5g",
        "sugar": "8g",
        "sodium": "600mg",
        "cholesterol": "75mg"
        }
    return prediction

def upload_image(request):
    if request.method=='POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            saved_image = form.save()
            #pass the image to model
            #take response from model
            #make the response part of the context and render it.
            response = predict("apple")
    else:
        form = UploadFileForm()
    return render(request,'track.html',{'form':form, 'response':response, 'fooditem':saved_image.image.url})

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

def track(request):
    form=UploadFileForm()
    return render(request, 'track.html', {'form':form})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Food, Contact
from .forms import UploadFileForm
import torch
from torchvision import models,transforms,datasets
from PIL import Image
import requests
import json
from django.conf import settings
from google.cloud import vision

#Load And Set ML model

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
loaded_model = models.resnet50(weights=None)  # Define the architecture
loaded_model.fc = torch.nn.Linear(loaded_model.fc.in_features, 101)  # Adjust for your dataset
loaded_model.load_state_dict(torch.load('img_classifier3.pth',map_location=device))  # Load the saved weights
loaded_model.to(device)  # Move the model to the appropriate device
loaded_model.eval()

data_transforms = {
    'train': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]),
    'val': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]),
}
BASE_URL = BASE_URL = "https://api.nal.usda.gov/fdc/v1/"

labels = datasets.Food101(root='./data', split='test', download=True, transform=data_transforms['val']).classes

def index(request):
    return render(request, 'index.html')

def is_food_image(image_path):
    """Check if the image contains food using Google Vision API."""
    client = vision.ImageAnnotatorClient()

    with open(image_path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    # Perform label detection
    response = client.label_detection(image=image)
    labels = response.label_annotations

    # Check if any label indicates food
    for label in labels:
        if "food" in label.description.lower() or "dish" in label.description.lower():
            return True
    return False


def fetchNutritionalProfile(food_name):
    food_name=food_name.replace("_"," ")

    search_url = f"{BASE_URL}foods/search?query={food_name}&api_key={settings.API_KEY}"
    response = requests.get(search_url)
    
    if response.status_code == 200:
        data = response.json()
        if data['foods']:
            food_data = data['foods'][0]
            food_id = food_data['fdcId']
            detail_url = f"{BASE_URL}food/{food_id}?api_key={settings.API_KEY}"
            detail_response = requests.get(detail_url)
            if detail_response.status_code == 200:
                detail_data = detail_response.json()
                nutrients = detail_data.get('foodNutrients', [])
                nutrition_info={'Food':food_name,"Portion Size":f"{detail_data.get('servingSize')} {detail_data.get('servingSizeUnit')}"}
                for dict in nutrients:
                    if dict["type"]=="FoodNutrient": 
                        nutrition_info[ dict["nutrient"]["name"] ] = f"{dict["amount"]} {dict["nutrient"]["unitName"]}"
                return nutrition_info
        else:
            print("Food item not found.")
    else:
        print("Error in the API request.",response.status_code)
    return None

def predict(image_path):
    image = Image.open(image_path).convert('RGB')
    image = data_transforms['val'](image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = loaded_model(image)
        _, predicted = torch.max(outputs, 1)
        predicted_label = labels[predicted.item()]
    return predicted_label

def upload_image(request):
    if request.method=='POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            saved_image = form.save()
            if is_food_image(saved_image.image.path):
                response = fetchNutritionalProfile(predict(saved_image.image.path))
                response["IsFoodImage"]=True
            else:
                response = {"IsFoodImage":False}
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
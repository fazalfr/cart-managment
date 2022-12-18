from django.shortcuts import render
from .models import users
from .models import Item
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'register.html')

def success(request):
    fullname = request.POST['fullname']
    username = request.POST['username']
    email  = request.POST['email']
    phone = request.POST['phone']
    password = request.POST['password']
    data = users(fullname=fullname,username=username,email=email,phone=phone,password=password)
    data.save()
    return render(request,'success.html')

def task(request):
    username2 = request.POST['l_username']
    password2 = request.POST['l_password']
    users.objects.filter(username=username2, password=password2)
    if username2 == 'admin' and password2 == 'admin':
        return render(request, 'admin.html')
    elif users.objects.filter(username=username2, password=password2):
        request.session['l_username'] = username2
        messages.info(request, "Logged in Successfully")
        return render(request, 'index.html')
    else:
        return render(request, 'error.html')

def index(request):
    return render(request,'index.html')

def form(request):
    return render(request,'form.html')

def pay(request):
    return render(request,'pay.html')

def main(request):
    return render(request,'main.html')

def add(request):
    return render(request,'add.html')

def added(request):
    name = request.POST['name']
    rate  = request.POST['rate']
    photo = request.FILES['photo']
    data = Item(name=name,rate=rate,photo=photo)
    data.save()
    return render(request,'added.html')

def show(request):
    data = Item.objects.all()
    return render(request, 'show.html', {'data': data})

def edit(request):
    return render(request,'edit.html')
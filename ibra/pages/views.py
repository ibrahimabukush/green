from django.shortcuts import render ,  redirect
from .models import Signnup
from .models import Contact
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib  import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        signup_data = Signnup(name=name, username=username, email=email, password=password)
        signup_data.save()
    return render(request, 'signup.html')

def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name1')
        email = request.POST.get('email1')
        report = request.POST.get('report1')
        contact.name = name
        contact.email = email
        contact.report = report
        contact.save()
        
        return render(request, 'contact.html')
    
    return render(request, 'contact.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')

def Logout_user(request):
    logout(request)
    messages.success(request,("you get out"))
    return redirect('home')
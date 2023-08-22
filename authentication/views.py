from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout

# Create your views here.

def register(request):
    # fetch data from signup form
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"] 
        cpassword = request.POST["cpassword"]
        
    #Jesus@pass4sure2023
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                print('Username Taken')
                messages.warning(request, 'Oops😥. Username Already Taken!')
                return render(request, 'authentication/register.html')
 
            elif User.objects.filter(email=email).exists():
                print('email Taken')
                messages.warning(request, 'Too bad😶. Email Already Exist!')
                return render(request, 'authentication/register.html')
                              
            else:
                user = User.objects.create_user(username=username, password=cpassword, email=email, first_name=fname, last_name=lname)
                #user.is_active = False
                user.save()
                auth.login(request, user)
                print('User created')
                return redirect('home')
        
        else:
            print('Password does not match')
            messages.error(request, 'Password Does Not Match!')
            return render(request, 'authentication/register.html')
        
    return render(request, "authentication/register.html")

# login views and functions
def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['username']
       
       user = auth.authenticate(username=username, password=password)
       if user is not None:
           auth.login(request, user)
           return redirect('home')
       else:
           messages.warning(request, "Incorrect Credentials. Please check your credentials again and try again!")
           return render(request, 'authentication/login.html')
    return render(request, "authentication/login.html") 

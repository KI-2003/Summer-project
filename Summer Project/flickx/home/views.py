from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
# Create your views here.
def start(request) :
    return render(request, "home/personalchats.html")

def homepage(request) :
    return render(request, "home/homepage.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirmpass = request.POST['confirmpass']
        email = request.POST['email']


        if User.objects.filter(username=username):
            messages.error(request, "Username already exists")
            return redirect('signup')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered")
            return redirect('signup')

        if(password!=confirmpass):
            messages.error(request, "Password didn't match")
            return redirect('signup')



        xuser = User.objects.create_user(username, email, password)
        xuser.username = username
        xuser.password = password
        xuser.email = email
        xuser.save()
        
        messages.success(request, "Account has been created!")

        return redirect('homepage')
    
    return render(request,'home/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,"home/personalchats.html")

        else:
            messages.error(request, "No user found")
            return redirect('homepage')
    return render(request, "home/homepage.html")

                


    





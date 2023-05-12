from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from accounts.forms import RegistrationForm




def register_view(request):
    user = request.user
    if user.is_authenticated:
      return HttpResponse(f"you are already authenticated as {user.username}.")
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = aunthenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            
            return redirect("home")

    
    return render(request,'accounts/register.html')    
        
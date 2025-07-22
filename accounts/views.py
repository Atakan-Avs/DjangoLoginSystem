from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request , username=username , password=password)
            if user:
                login(request, user)
                return redirect('welcome')
            else:
                messages.error(request , 'Kullanıcı adı veya şifre hatalı.')
    else:
        form = LoginForm()
    return render(request , 'accounts/login.html' , {'form' : form})

@login_required
def welcome_view(request):
    return render(request , 'accounts/welcome.html')

def logout_view(request):
    logout(request)
    return redirect('login')


# accounts/views.py

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

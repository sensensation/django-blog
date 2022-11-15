from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from .forms import *


class Auth():
    @staticmethod
    def register_user(request):
        if request.user.is_authenticated == True:
            return redirect('index')

        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.set_password(user.password)
                user.save()
                return redirect('login_page')
            
        form = UserRegisterForm()
        context = { 'form': form }

        return render(request, 'registration/signup.html', context)
    
    @staticmethod
    def login_user(request):
        if request.user.is_authenticated == True:
            return redirect('index')

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(
                request, 
                username=username, 
                password=password
            )
            if user is not None:
                login(request, user)
                return redirect('index')
            
        form = UserLoginForm()
        context = { 'form': form }

        return render(request, 'registration/login.html', context)
            
    @staticmethod
    def logout_user(request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('login')
        return redirect('index')
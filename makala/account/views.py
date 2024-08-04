from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
       form = CustomUserCreationForm(request.POST)
       if form.is_valid():
           print('Form is valid')
           user = form.save()
           return redirect('login')
       else:
            
            print('Form is not valid')
            return render(request,'register.html', {'form': form, 'errors': form.errors.as_text()})
           
    else:
        form = CustomUserCreationForm()
        return render(request,'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(request,username=username, password=password)
        if user is not None:
            print('User is authenticated')
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Ulanyjy ady yada parol nadogry'})
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth_logout(request)
    return redirect('index')

from django.shortcuts import render
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm

@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You have registered successfully!")
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/user_register.html', {'form': form})

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            messages.success(request, "You have registered successfully!")
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Login failed. Please correct the errors below.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/user_login.html', {'form': form})


@csrf_exempt
def user_logout(request):
    logout(request)
    return redirect('index')

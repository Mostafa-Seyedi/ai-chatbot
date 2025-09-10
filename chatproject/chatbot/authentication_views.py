from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register_view(request):
    """This view handles user registration (creating new accounts)"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # UserCreationForm is Django's built-in form for creating users
        
        if form.is_valid():
            # Create the new user
            user = form.save()
            
            # Log them in automatically after registration
            login(request, user)
            
            # Show success message
            messages.success(request, 'Account created successfully!')
            
            # Redirect to chatbot page
            return redirect('chatbot')
    else:
        # If GET request (just viewing the page), show empty form
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    """This view handles user login"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Check if username and password are correct
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Username and password are correct
            login(request, user)  # Log them in
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('chatbot')
        else:
            # Wrong username or password
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'registration/login.html')

def logout_view(request):
    """This view handles user logout"""
    logout(request)  # Log them out
    messages.info(request, 'You have been logged out.')
    return redirect('login')
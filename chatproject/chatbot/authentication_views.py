from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy

def register_view(request):
    """This view handles user registration (creating new accounts)"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            # Create the new user
            user = form.save()
            
            # Log them in automatically after registration
            login(request, user)
            
            # Show success message
            messages.success(request, f'Welcome {user.username}! Your account has been created successfully.')
            
            # Redirect to chatbot page
            return redirect('chatbot')
        else:
            # Form has errors - they will be displayed in the template
            messages.error(request, 'Please correct the errors below.')
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
            
            # Check if there's a 'next' parameter (redirect after login)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('chatbot')
        else:
            # Wrong username or password
            messages.error(request, 'Invalid username or password. Please try again.')
    
    return render(request, 'registration/login.html')

def logout_view(request):
    """This view handles user logout"""
    # Store username before logging out (for personalized message)
    if request.user.is_authenticated:
        username = request.user.username
        user_was_logged_in = True
    else:
        username = "Guest"
        user_was_logged_in = False
    
    # Log the user out
    logout(request)
    
    # Add a goodbye message
    if user_was_logged_in:
        messages.info(request, f'Goodbye {username}! You have been logged out successfully.')
    else:
        messages.info(request, 'You have been logged out.')
    
    # Render the logout template instead of redirecting
    return render(request, 'registration/logout.html', {
        'username': username,
        'was_logged_in': user_was_logged_in
    })

# Optional: Add a view to handle the home page redirect
def home_view(request):
    """Handle home page - redirect based on authentication status"""
    if request.user.is_authenticated:
        # User is logged in, redirect to chatbot
        return redirect('chatbot')
    else:
        # User is not logged in, redirect to login page
        return redirect('login')
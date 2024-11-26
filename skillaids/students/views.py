from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from students.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile




def volunteers_home(request):
    return render(request, 'volunteer.html')

def profile(request):
    return render(request, 'profile.html')

def login_view(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']
        
        # Try to authenticate using either username or email
        user = authenticate(request, username=user_id, password=password)
        
        if user is not None:
            login(request, user)
            #messages.success(request, 'Login successful!')
            return redirect('homepage')  # Replace with your homepage URL name
        else:
            # Check if the user exists but password is wrong
            try:
                # Check if user exists by username or email
                user_exists = User.objects.filter(username=user_id) or User.objects.filter(email=user_id)
                
                if user_exists:
                    messages.error(request, 'Invalid password. Please try again.')
                else:
                    messages.error(request, 'User does not exist. Please sign up.')
            except:
                messages.error(request, 'Login failed. Please try again.')
            
            return render(request, 'signup.html')
    
    return render(request, 'signup.html')

def signup_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')
        
        # Validate inputs
        if not (user_id and full_name and email and password and confirm_password and role):
            messages.error(request, 'All fields are required.')
            return render(request, 'signup.html')
        
        # Check if user already exists
        if User.objects.filter(username=user_id).exists() or User.objects.filter(email=email).exists():
            messages.error(request, 'User with this ID or email already exists.')
            return render(request, 'signup.html')
        
        # Validate password
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')
        
        # Create user
        try:
            user = User.objects.create_user(
                username=user_id, 
                email=email, 
                password=password,
                first_name=full_name
            )
            user.save()
            # Create user profile with role-specific details
            if role == 'mentee':
                profile_data = {
                    'age': request.POST.get('age'),
                    'education': request.POST.get('education'),
                    'skills': request.POST.get('skills'),
                    'preferred_days': request.POST.get('preferred_days')
                }
            elif role == 'mentor':
                profile_data = {
                    'company_affiliation': request.POST.get('company_affiliation'),
                    'role_at_company': request.POST.get('role_at_company'),
                    'professional_expertise': request.POST.get('professional_expertise'),
                    'area_of_interest': request.POST.get('area_of_interest'),
                    'preferred_communication': request.POST.get('preferred_communication')
                }
            else:
                messages.error(request, 'Invalid role selected.')
                return render(request, 'signup.html')
            
            # Create UserProfile
            UserProfile.objects.create(
                user=user,
                role=role,
                **profile_data
            )
            
            # Authenticate and login
            authenticated_user = authenticate(username=user_id, password=password)
            if authenticated_user:
                login(request, authenticated_user)
                messages.success(request, 'Account created successfully!')
                return redirect('homepage')  # Replace with your homepage URL name
        
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return render(request, 'signup.html')
    
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('homepage')  # Replace with your homepage URL name



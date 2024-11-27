from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from students.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password





def profile(request):
    return render(request, 'profile.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user =  authenticate(request,username=username, password=password)
       
        if user is not None and user.is_active:

            if user.is_superuser:
                login(request, user)
                return redirect('admin')

            details = userdetails.objects.get(user = user)
           
            # if details.user_type == 'Official':
            #     login(request, user)
            #     return redirect('official-profile')

            if details.user_type == 'mentee':
                login(request, user)
                return redirect('events')
                
            elif details and details.user_type == 'mentor':
                login(request, user)
                return redirect('volunteer')
            
        else:
            msg = "wrong Credentials"
            return render(request, 'signup.html', {'msg': msg})
    return render(request, 'signup.html')


# def admin_dashboard(request):
#     # admin_dashboard.html needs to be added
#     return render(request, 'Admin/admin-dashboard.html')


def register(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']  
        email = request.POST['email']
        phone = request.POST['phone']
        role = request.POST['role']
        password = request.POST['password1']
        
        user = User(
            username=username,  # Include the username parameter
            email=email,
            password=make_password(password),
            first_name=firstName,
            last_name=lastName,
        )
        
        user.save()
        print(f"User created: {user.__dict__}")

        user_details = userdetails(user_id=user.id, user_phone=phone, user_type=role)
        user_details.save()
        user_model = User.objects.get(username=username)
        return redirect('userlogin')

    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('homepage')  # Replace with your actual homepage URL name

def volunteers_list(request):
    volunteers = Volunteer.objects.all()
    print(volunteers)
    return render(request, 'volunteer.html', {'volunteers': volunteers})
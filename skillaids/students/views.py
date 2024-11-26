from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from students.models import User_PhoneNumber
from django.contrib.auth import authenticate, login, logout

# User Authentication View
def user_authentication(request):
    if request.method == 'POST':
        if 'signin' in request.POST:
            email = request.POST['login_email']
            password = request.POST['login_password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                error_message = 'Invalid Password' if User.objects.filter(username=email).exists() else 'User does not exist'
                return render(request, 'user_authentication/user_authentication.html', {'signin_error_message': error_message})
        
        elif 'signup' in request.POST:
            name = request.POST['signup_name']
            email = request.POST['signup_email']
            phone = request.POST['signup_phone']
            password = request.POST['signup_password']
            confirm_password = request.POST['signup_confirm_password']
            
            if (User.objects.filter(username=email).exists() or 
                User.objects.filter(email=email).exists() or 
                User_PhoneNumber.objects.filter(phoneNumber=phone).exists()):
                return render(request, 'skillaids/template/signup.html', {'signup_error_message': 'User Already Exists'})
            
            if password != confirm_password:
                return render(request, 'skillaids/template/signup.html', {'signup_error_message': 'Password did not match'})
            
            user = User.objects.create_user(first_name=name, username=email, email=email, password=password)
            user.save()
            user_phone = User_PhoneNumber(user=user, phoneNumber=phone)
            user_phone.save()
            return redirect('homepage')
    
    return render(request, 'skillaids/template/signup.html')

# User Logout
def user_logout(request):
    logout(request)
    return redirect('homepage')

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from students.models import User_PhoneNumber
from django.contrib.auth import authenticate, login,logout


# Create your views here.

def user_authentication(request):
    if request.method == 'POST':
        if 'signin' in request.POST:
            email = request.POST['login_email']
            password = request.POST['login_password']
            user = authenticate(username = email,password = password)
            if user is not None:
                login(request,user)
                return redirect('homepage')
            else:
                if User.objects.filter(username = email).exists() or User.objects.filter(email = email).exists():
                    return render(request,'user_authentication/user_authentication.html',{'signin_error_message':'Invalid Password'})
                else:
                    return render(request,'user_authentication/user_authentication.html',{'signin_error_message':'User does not Exist'})
        elif 'signup' in request.POST:
            name = request.POST['signup_name']
            email = request.POST['signup_email']
            phone = request.POST['signup_phone']
            password = request.POST['signup_password']
            confirm_password = request.POST['signup_confirm_password']
            if ((User.objects.filter(username = email).exists()) 
            or (User.objects.filter(email = email).exists()) 
            or (User_PhoneNumber.objects.filter(phoneNumber = phone).exists())):
                return render(request,'user_authentication/user_authentication.html',{'signup_error_message':'User Already Exists'})
            elif password != confirm_password:
                return render(request,'user_authentication/user_authentication.html',{'signup_error_message':'Password did not Match'})
            else:
                user = User.objects.create_user(first_name = name,username = email,email = email,password = password)
                user.save()
                user_phone = User_PhoneNumber(user = user,phoneNumber = phone)
                user_phone.save()
                return redirect('homepage')
    return render(request,'user_authentication/user_authentication.html')

def user_logout(request):
    logout(request)
    return redirect('homepage')



    

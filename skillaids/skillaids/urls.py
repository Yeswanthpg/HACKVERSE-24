"""
URL configuration for skillaids project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students import views as students_views
from events.views import *
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: render(request, 'homepage.html'), name='homepage'),
    path('login/', students_views.login_view, name='signin'), 
    path('signup/', students_views.signup_view, name='signup'),  # Corrected to signup_view
    path('logout/', students_views.logout_view, name='user_logout'),  # Corrected to logout_view
    path('students/', students_views.volunteers_home, name='volunteers_home'),
    path('students/profile/', students_views.profile, name='profile'),
    path('events/', events_home, name='events'),  # Updated name
    path('volunteer/', students_views.volunteers_home, name='volunteer'),  # Added pattern
]



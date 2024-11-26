from django.contrib import admin
from .models import Student, User_PhoneNumber, UserProfile

# Register UserProfile model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture')
    search_fields = ('user__username', 'bio')
    list_filter = ('user',)

# Register User_PhoneNumber model
@admin.register(User_PhoneNumber)
class UserPhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('user', 'phoneNumber')
    search_fields = ('user__username', 'phoneNumber')

# Register Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'email', 'skills', 'experience_level', 'location')
    search_fields = ('name', 'email')
    list_filter = ('skills', 'experience_level', 'location')
    ordering = ('student_id',)


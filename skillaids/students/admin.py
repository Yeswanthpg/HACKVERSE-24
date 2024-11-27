from django.contrib import admin
from .models import userdetails, Volunteer

# Register your models here.

admin.site.register(userdetails)


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    # Customize the list view in the admin panel
    list_display = ('student_id', 'name', 'email', 'experience_level', 'location')
    search_fields = ('name', 'skills', 'email', 'location')
    list_filter = ('experience_level', 'location')
from django.contrib import admin
from .models import Event

# Register the Event model so it can be managed in the Django admin interface
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'event_category', 'event_date')
    search_fields = ('event_title', 'event_category', 'skills_required')
    list_filter = ('event_category',)

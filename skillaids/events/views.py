from django.shortcuts import render
from .models import Event

def events_home(request):
    # Get all events, or filter them if a category is provided
    category_filter = request.GET.get('category', None)
    
    if category_filter:
        events = Event.objects.filter(event_category=category_filter)
    else:
        events = Event.objects.all()  # Fetch all events

    return render(request, 'events.html', {'events': events})

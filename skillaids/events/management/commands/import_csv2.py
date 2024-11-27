import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from events.models import Event
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = 'Import events from a CSV file'

    def handle(self, *args, **kwargs):
        with open('event_data.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Ensure the event_date is in the correct format (YYYY-MM-DD)
                try:
                    # Check if the date is in DD-MM-YYYY format and convert it to YYYY-MM-DD
                    event_date_str = row['event_date'].strip()  # Remove any leading/trailing spaces
                    event_date = datetime.strptime(event_date_str, "%d-%m-%Y").strftime("%Y-%m-%d")
                    
                    # Create or update the Event record
                    Event.objects.update_or_create(
                        event_id=row['event_id'],  # Ensure `event_id` is used as a unique identifier
                        defaults={
                            'event_title': row['event_title'],
                            'event_description': row['event_description'],
                            'skills_required': row['skills_required'],
                            'event_category': row['event_category'],
                            'event_date': event_date,  # Use the correctly formatted event_date
                            'location': row['location'],
                        }
                    )
                except ValueError:
                    raise ValidationError(f"Invalid date format for event_id {row['event_id']}: {row['event_date']}")
                
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))

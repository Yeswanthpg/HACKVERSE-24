import csv
from django.core.management.base import BaseCommand
from students.models import Volunteer

class Command(BaseCommand):
    help = 'Import volunteers from a CSV file'

    def handle(self, *args, **kwargs):
        with open('dataSkillAids - Himali_Dataset.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Create or update the Volunteer record
                Volunteer.objects.update_or_create(
                    student_id=row['student_id'],  # Ensure `student_id` is used as a unique identifier
                    defaults={
                        'name': row['name'],
                        'skills': row['skills'],
                        'experience_level': int(row['experience_level']),
                        'location': row['location'],
                        'email': row['email'],
                    }
                )
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))

from django.db import models

# Create your models here.
class Event(models.Model):
    # Define fields for the event
    event_id = models.AutoField(primary_key=True)
    event_title = models.CharField(max_length=255)
    event_description = models.TextField()
    skills_required = models.TextField()  # Store skills as a string
    event_category = models.CharField(max_length=100)
    event_date = models.DateField()
    location = models.CharField(max_length=100, default="Unknown Location")
    image_url = models.URLField(blank=True, null=True)  # Added an image URL field

    def __str__(self):
        return self.event_title

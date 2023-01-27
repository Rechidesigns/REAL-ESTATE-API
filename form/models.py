from django.db import models
from django.forms import ModelForm
from phonenumber_field.modelfields import PhoneNumberField

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]


INSPECTION_CHOICES = [
    ('EARLY WEEK', 'Mondays & Tuesdays.'),
    ('MIDWEEK', 'Wednesdays & Thursdays.'),
    ('WEEKEND', 'Fridays, Saturdays $ Sundays.'),
]

TIME_CHOICES = [
    ('MORNING', '7AM - 12PM.'),
    ('EVENING', '12PM - 6PM.'),
]

class BookInspection(models.Model):
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    inspection_schedule = models.CharField(max_length=50, choices=INSPECTION_CHOICES)
    prefered_time = models.CharField(max_length=20, choices=TIME_CHOICES)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Houses(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    num_of_rums = models.IntegerField()
    address = models.CharField(max_length=150)
    phone = PhoneNumberField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lands(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    num_of_plot = models.CharField(max_length=150)
    square_footage = models.CharField(max_length=250)
    location = models.CharField(max_length=150)
    phone = PhoneNumberField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


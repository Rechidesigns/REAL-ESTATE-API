from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class HouseImages(models.Model):
    image = models.ImageField(upload_to='house_images/')
    name = models.CharField(max_length=100)

class Houses(models.Model):
    images = models.ManyToManyField(HouseImages, related_name='houses')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    num_of_rums = models.IntegerField()
    address = models.CharField(max_length=150)
    phone = PhoneNumberField()
    price = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class LandImages(models.Model):
    image = models.ImageField(upload_to='lands_images/')
    name = models.CharField(max_length=100)


class Lands(models.Model):
    images = models.ManyToManyField(LandImages, related_name='houses')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    num_of_plot = models.CharField(max_length=150)
    square_footage = models.CharField(max_length=250)
    location = models.CharField(max_length=150)
    phone = PhoneNumberField()
    price = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator, MinValueValidator


class Recuiters(models.Model):
    full_name = models.CharField(max_length=100, validators=[
        RegexValidator(r'^[a-zA-Z ]*$', 'Only letters and spaces are allowed.')
    ])
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True, validators=[
        RegexValidator(r'^\d{10}$', 'Only 10 digits are allowed.')
    ])
    city = models.CharField(max_length=100, validators=[
        RegexValidator(r'^[a-zA-Z0-9 ,.\'-]*$',
                       'Only letters, numbers, spaces, commas, periods, apostrophes and hyphens are allowed.')
    ])
    age = models.PositiveIntegerField(validators=[
        MinValueValidator(0, 'Age cannot be negative.')
    ])
    summary = models.TextField()
    company = models.TextField()
    photo = models.ImageField(upload_to='media', blank=True, null=True, validators=[
        FileExtensionValidator(['jpg', 'jpeg', 'png', 'gif'],
                               'Only jpg, jpeg, png and gif files are allowed.')
    ])

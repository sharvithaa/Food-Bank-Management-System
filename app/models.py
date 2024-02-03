from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USERTYPE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('ngo', 'NGO'),
        ('donor', 'Donor'),
    ]
    usertype = models.CharField(
        max_length=10,
        choices=USERTYPE_CHOICES,
        default='donor'
    )

class FoodDonation(models.Model):
    foodname = models.CharField(max_length=100)
    email = models.EmailField()
    phoneno = models.CharField(max_length=15)
    is_veg = models.BooleanField(default=False)
    is_nonveg = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField()
    address = models.TextField()
    donation_date = models.DateField(default=timezone.now)  # Date field for donation date
    donation_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.foodname

class Order(models.Model):
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    food_donation = models.ForeignKey(FoodDonation, on_delete=models.CASCADE)  # Add this line
    product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    place = models.CharField(max_length=1000, default="Erode")
    
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    quantity = models.IntegerField()
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rooms_choice=[
        ('Room1','Room1'),
        ('Room2',"Room2"),
        ('Room3',"Room3"),
        
    ]
    room = models.CharField(max_length=20, choices=rooms_choice, default='Room1')
    beds_choice = [
        ('BedNo:1', 'BedNo:1'),
        ('BedNo:2', 'BedNo:2'),
        ('BedNo:3', 'BedNo:3'),
    ]
    name = models.CharField(max_length=20, choices=beds_choice,default="BedNo:1")
    age = models.IntegerField(null=True)
    date = models.DateField(null=True)
    approved = models.BooleanField(default=False)
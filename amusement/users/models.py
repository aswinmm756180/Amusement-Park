from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adhar_number = models.CharField(max_length=12)
    location = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, choices=[('student', 'Student'), ('working', 'Working')])
    phone_number = models.CharField(max_length=10)
    age = models.IntegerField()
    parents_contact=models.CharField(max_length=12,null=True,blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.user.username



class Bookticket(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
def __str__(self):
    return self.name


# class Booking(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     rooms_choice=[
#         ('Room1','Room1'),
#         ('Room2',"Room2"),
#         ('Room3',"Room3"),
#         ('Room4',"Room4"),
#         ('Room5',"Room5"),
#         ('Room6',"Room6"),

#     ]
    # room = models.CharField(max_length=20, choices=rooms_choice, default='Room1')
    # beds_choice = [
    #     ('BedNo:1', 'BedNo:1'),
    #     ('BedNo:2', 'BedNo:2'),
    #     ('BedNo:3', 'BedNo:3'),
    #     ('BedNo:4', 'BedNo:4'),
    #     ('BedNo:5', 'BedNo:5'),
    # ]
    # bed = models.CharField(max_length=20, choices=beds_choice,default="BedNo:1")
    # time = models.DateTimeField(null=True)
    # date = models.DateField(null=True)
    # approved = models.BooleanField(default=False)
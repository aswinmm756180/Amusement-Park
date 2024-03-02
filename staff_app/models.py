from django.db import models

# Create your models here.


Food_categories=(
    ('BreakFast','BreakFast'),
    ('Lunch','Lunch'),
    ('Tea','Tea'),
    ('Dinner','Dinner'),

)
class Foodlist(models.Model):
    food_id=models.AutoField(primary_key=True)
    food_name=models.CharField(max_length=200)
    food_image=models.ImageField(null=True,blank=True,upload_to="foods")
    Food_category=models.CharField(max_length=200,choices=Food_categories,default='Lunch')
    
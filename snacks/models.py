from django.db import models
from django.db.models.fields import CharField



# Create Snack model
# title field
# purchaser field
# description field
# Register model with admin
# Create your models here.
class Snack(models.Model):
    title=models.CharField(max_length=256)
    purchaser=models.CharField(max_length=64)
    describtion=models.CharField(max_length=256)
    


   
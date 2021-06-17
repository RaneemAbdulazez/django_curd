from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth import get_user_model

from django.urls import reverse



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
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("detail_view", args=[str(self.id)])

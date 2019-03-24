from django.db import models

# Create your models here.
class Publisher(models.Model):
    pub_name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
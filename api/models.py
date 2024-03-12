from django.db import models

# Create your models here.


class Mobile(models.Model):
    name=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    descritpiom=models.CharField(max_length=50)
    image=models.ImageField(null=True,blank=True,upload_to='images')

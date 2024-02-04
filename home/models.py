from django.db import models

# Create your models here.
class Rm(models.Model):
    r_name = models.CharField(max_length = 50)
    r_des  = models.CharField(max_length = 50)
    r_img = models.ImageField(upload_to='receipe')

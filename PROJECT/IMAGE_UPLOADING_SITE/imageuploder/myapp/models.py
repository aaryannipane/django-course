from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to='myimg')
    date = models.DateTimeField(auto_now_add=True)
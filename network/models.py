from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


class User(AbstractUser):
    identification = models.CharField(max_length=9, null=True, blank=True)
    photo = models.ImageField(upload_to="images/", default="images/default_image.png")

class Module(models.Model):
    module_code = models.CharField(max_length=30, null=True, blank=True)
    module_name = models.CharField(max_length=200, null=True, blank=True)
    module_summary = models.CharField(max_length=3000, null=True, blank=True)
    def __str__(self):
        return self.module_code

class Review(models.Model):
    module_code = models.CharField(max_length=30, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.IntegerField(blank=True, null=True)
    semester = models.IntegerField(choices=(("1",1),("2",2)), default=1)
    professor = models.CharField(max_length=500, null=True, blank=True)
    review = models.TextField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.user.username
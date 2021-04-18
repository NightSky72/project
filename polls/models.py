from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

class Teacher(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    code = models.TextField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    Name = models.CharField(max_length=20, null=True)
    Otchestvo = models.CharField(max_length=20, null=True)
    Phone = models.CharField(max_length=20, null=True)
     # photo = models. ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    Surname = models.CharField(max_length=20, null=True)
    name_class = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.Surname
    objects = models.Manager()

# class Albums(models.Model):
#     name_of_album = models.CharField(max_length=20)


class Photo(models.Model):
    # id_name_of_album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/')


class Schedule(models.Model):
    id_teacher_id = models.IntegerField(null=True)
    number = models.CharField(max_length=3, null=True)
    name_class = models.CharField(max_length=20, null=True)
    time_class = models.CharField(max_length=20, null=True)
    week_day = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.number
    objects = models.Manager()



# class Hotel(models.Model):
#     name = models.CharField(max_length=50)


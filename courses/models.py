from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

class Course(models.Model):
    name= models.CharField(max_length=200)
    desc = models.TextField()
    teacher = models.CharField(max_length=50)
    classTime = models.CharField(max_length=200)
    capacity = models.IntegerField()

    def __str__(self):
        return self.title

class User(models.Model):
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.firstName+self.lastName

class EnrollList(models.Model):
    courseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.courseId)

# Create your models here.

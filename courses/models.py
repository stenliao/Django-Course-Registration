from django.db import models
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User

class Course(models.Model):
    DAYS_OF_WEEK = (
        (1, 'Sunday'),
        (2, 'Monday'),
        (3, 'Tuesday'),
        (4, 'Wednesday'),
        (5, 'Thursday'),
        (6, 'Friday'),
        (7, 'Saturday'),
    )
    DATE_OF_DAY = (
        (8, '08:00'),
        (9, '09:00'),
        (10, '10:00'),
        (11, '11:00'),
        (12, '12:00'),
        (13, '13:00'),
        (14, '14:00'),
        (15, '15:00'),
        (16, '16:00'),
        (17, '17:00'),
        (18, '18:00'),
    )
    name= models.CharField(max_length=200)
    desc = models.TextField()
    teacher = models.CharField(max_length=50)
    weekday = models.IntegerField(choices=DAYS_OF_WEEK,default=1)
    start = models.IntegerField(choices=DATE_OF_DAY,default=1)
    end = models.IntegerField(choices=DATE_OF_DAY,default=1)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

# class User(models.Model):
#     userName = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     firstName = models.CharField(max_length=50)
#     lastName = models.CharField(max_length=50)
#     email = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.firstName+self.lastName
class EnrollManager(models.Manager):
    def isExist(self, coursePK, userPK):
        course = get_object_or_404(Course, pk=coursePK)
        user = get_object_or_404(User, pk=userPK)
        e = EnrollList.objects.filter(courseId=course)
        e.filter(userId=user)
        return e.count()>0

class EnrollList(models.Model):
    courseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    objects = EnrollManager()

    # @classmethod
    # def create(cls, coursePK, userPK):
    #     book = cls(courseId=coursePK, userId=userPK)
    #     # do something with the book
    #     return book

    def __str__(self):
        return str(self.courseId)



# Create your models here.

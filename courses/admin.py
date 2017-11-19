from django.contrib import admin
from .models import Course
from .models import User
from .models import EnrollList

# Register your models here.
admin.site.register(Course)
admin.site.register(User)
admin.site.register(EnrollList)

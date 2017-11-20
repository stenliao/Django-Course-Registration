from django import forms

from .models import Course
# from .models import User

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('number','name', 'desc', 'instructor','weekday','start','end', 'capacity','unit','room')

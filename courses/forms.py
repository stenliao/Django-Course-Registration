from django import forms

from .models import Course
# from .models import User

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'desc', 'teacher','weekday','start','end', 'capacity')
        #widgets = { 'weekday': forms.ChoiceField}


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('userName', 'password', 'firstName', 'lastName', 'email')
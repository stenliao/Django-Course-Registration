from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import CourseForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
import json

def course_list(request):
    courses = Course.objects.filter().order_by('id')
    print courses
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def course_new(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('courses.views.course_detail', pk=course.pk)
    else:
        form = CourseForm()
    return render(request, 'courses/course_edit.html', {'form': form})
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('courses.views.course_detail', pk=course.pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_edit.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Course
from .models import EnrollList
from .forms import CourseForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User

import json

def course_list(request):
    courses = Course.objects.filter().order_by('id')
    print courses
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    isExist = EnrollList.objects.isExist(pk, request.user.pk)
    print isExist
    return render(request, 'courses/course_detail.html', {'course': course, 'isExist': isExist})

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

def course_register(request, pk, upk):
    course = get_object_or_404(Course, pk=pk)
    user = get_object_or_404(User, pk=upk)
    isExist = EnrollList.objects.isExist(pk, upk)
    print isExist
    if isExist == False:
        enroll = EnrollList.objects.create(courseId=course, userId=user)
        enroll.save()
        return redirect('courses.views.course_detail', pk=pk)
    else:
        return redirect('courses.views.course_detail', pk=pk)
def course_deregister(request, pk, upk):
    course = get_object_or_404(Course, pk=pk)
    user = get_object_or_404(User, pk=upk)
    isExist = EnrollList.objects.isExist(pk, upk)
    print isExist
    if isExist == True:
        enroll = EnrollList.objects.filter(courseId=course, userId=user)
        print enroll
        enroll.delete()
        return redirect('courses.views.course_detail', pk=pk)
    else:
        return redirect('courses.views.course_detail', pk=pk)
# def user_list(request):
#     users= User.objects.filter().order_by('id')
#     return render(request, 'courses/user_list.html', {'users': users})
#
# def user_detail(request, pk):
#     user= get_object_or_404(User, pk=pk)
#     return render(request, 'courses/user_detail.html', {'user': user})
#
# def user_new(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
#             return redirect('courses.views.user_detail', pk=user.pk)
#     else:
#         form = UserForm()
#     return render(request, 'courses/user_edit.html', {'form': form})
#
# def user_edit(request, pk):
#     user= get_object_or_404(User, pk=pk)
#     if request.method == "POST":
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             user= form.save(commit=False)
#             user.save()
#             return redirect('courses.views.user_detail', pk=user.pk)
#     else:
#         form = UserForm(instance=user)
#     return render(request, 'courses/user_edit.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction

from .models import Course
from .forms import FormCourse, FormDescription, FormComment

"""
To Dos
- Make update Function
- Make Comment functionality
- Make view one course functionality

"""

# Create your views here.

"""
View that lists all created Courses and their description as well as a 
form to create new Courses and link their description models to the newly made course
"""

def CourseCreateListView(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = FormCourse(request.POST)
        descr_form = FormDescription(request.POST)
        if form.is_valid() and descr_form.is_valid():
            with transaction.atomic():
                course_instance = form.save()
                description_instance = descr_form.save(commit=False)
                description_instance.course = course_instance
                description_instance.save()
                return redirect('course-list')
    else:
        form = FormCourse()
        descr_form = FormDescription()

    context = {
        'form' : form,
        'description_form' : descr_form,
        'courses' : courses,
    }

    return render(request, 'courses/course_list.html', context)

def CourseDetails(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":
        comment_form = FormComment(request.POST)
        if comment_form.is_valid():
            comment_instance = comment_form.save(commit=False)
            comment_instance.course = course
            comment_instance.save()
            return redirect('course-detail', pk=course.id)
    comment_form = FormComment()

    context = {
        'course' : course,
        'form' : comment_form,
    }
    return render(request, 'courses/course_detail.html', context)


"""
View that takes grabs an object through its ID and redirects to a confirmation deletion page
and then deletes that object from the database
"""

def CourseDeleteView(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {
        'course' : course
    }

    return render(request, 'courses/course_confirm_delete.html', context)

def DeleteCourse(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect('course-list')


"""
These views are for creating comments under courses
"""

# Input: text submitted through a form
# Ouput: A course has a new comment object in its 'comments' attribute
# 




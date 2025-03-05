from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import *

# from .models import Course

# Create your views here.


def home(request):
    courses = Course.objects.all()
    return render(request,'home.html', {'courses': courses})
def courses(request):
    courses = Course.objects.all()
    return render(request,'courses.html',{'courses':courses})
def bootcamp(request):
    return render(request,'bootcamp.html')
def signin(request):
    return render (request,'signin.html')


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course_detail.html', {'course': course})

from django.apps import apps

# def course_list(request):
#     Course = apps.get_model('myapp1', 'Course')
#     courses = Course.objects.all()
#     return render(request, 'your_template.html', {'courses': courses})

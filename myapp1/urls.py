from django.urls import path
from .views import *
from . import views
app_name='myapp1'

urlpatterns = [
    path('',home ,name='home'),
    path('courses/',courses,name='courses'),
    path('bootcamp/',bootcamp,name='bootcamp'),
    path('signin/',signin,name='signin'),
     path('course/<int:course_id>/', views.course_detail, name='course_detail'),
]
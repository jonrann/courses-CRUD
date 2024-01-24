
from django.urls import path
from .views import CourseCreateListView, CourseDeleteView, DeleteCourse, CourseDetails

urlpatterns = [
    path('', CourseCreateListView, name='course-list' ),
    path('course/<int:pk>/delete', CourseDeleteView, name='course-delete'),
    path('course/<int:pk>/confirm_delete', DeleteCourse, name='course-destroy'),


    path('course/<int:pk>/details', CourseDetails, name='course-detail'),
    

]
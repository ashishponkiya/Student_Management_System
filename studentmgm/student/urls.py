from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('',views.dashboard, name='dashboard'),
    path('students/', views.Student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.add_course, name='add_course'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('courses/delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
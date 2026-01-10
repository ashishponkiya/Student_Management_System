from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render
from django.contrib import messages


# Create your views here.
from .models import Student, Course
from .forms import StudentForm, CourseForm, RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect(request.POST.get('next') or 'dashboard')
            else:
                messages.error(request, 'Invalid username or password!')
    else:
        form = LoginForm()

    return render(request, 'login.html', {
        'form': form,
        'next': request.GET.get('next')
    })


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    students = Student.objects.count()
    courses = Course.objects.count()
    all_students = Student.objects.all()
    all_courses = Course.objects.all()
    context = {
        'students': students,
        'courses': courses,
        'all_students': all_students,
        'all_courses': all_courses,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def Student_list(request):
    students= Student.objects.select_related()
    context={
        'students': students,
    }
    return render(request, 'student_list.html', context)

@login_required(login_url='login')
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

@login_required(login_url='login')
def course_list(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'course_list.html', context)

@login_required(login_url='login')
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully!')
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

@login_required(login_url='login')
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list')

@login_required(login_url='login')
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return redirect('course_list') 
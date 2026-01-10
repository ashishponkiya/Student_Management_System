from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=30)
    age = models.IntegerField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.full_name
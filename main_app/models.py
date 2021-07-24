from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.contrib.auth.models import User

# Student model 
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    teacher = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.first_name
    

class Assignment(models.Model):
    description = models.TextField(max_length=1000)
    due_date = models.DateField()
    # completed_date = models.DateField(null=True) 
    # teacher = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse('assignments_detail', kwargs={'pk': self.id})

class Classroom(models.Model):
    course_subject = models.CharField(max_length=100)
    course_number = models.IntegerField()
    course_name = models.CharField(max_length=100)
    # students = models.ManyToManyField(Student)
    # teacher = models.ForeignKey(User, on_delete=CASCADE)
    
    def __str__(self):
        return f'{self.course_subject} {self.course_number}, {self.course_name}'

    def get_absolute_url(self):
        return reverse('classroom_detail', kwargs={'pk': self.id})

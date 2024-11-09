from django.db import models
from adminapp.models import StudentList  # Importing the StudentList model


class AddCourse(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'Advanced Object-Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),
        ('OS','Operating Systems'),
        ('DBMS','Database Management Systems'),
        ('AIML','ArtificialIntelligence and machine learning')
    ]
    SECTION_CHOICES = [
        ('S11', 'Section S11'),
        ('S12', 'Section S12'),
        ('S13', 'Section S13'),
        ('S14', 'Section S14'),
        ('S15', 'Section S15'),
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)

    def str(self):
        return f'{self.student.Register_Number} - {self.course} ({self.section})'

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # Ensure this field exists

    def __str__(self):
        return self.title


class Marks(models.Model):
    COURSE_CHOICES=[
        ('AOOP', 'Advanced Object-Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),
        ('OS', 'Operating Systems'),
        ('DBMS', 'Database Management Systems'),
        ('AIML', 'ArtificialIntelligence and machine learning')
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    marks = models.IntegerField()
    def __str__(self):
        return f"{self.student.name} - {self.course}"



from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Permission

class Subject(models.Model):
    name = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    update_time = models.DateTimeField(auto_now = True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subject'
        permissions = (
                       ("read_subject", "Can read subject"), 
                       )

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    update_time = models.DateTimeField(auto_now = True, blank=True, null=True)
    subject = models.ForeignKey(Subject, unique=True)
    user = models.ForeignKey(User, blank = True, null = True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'teacher'
        permissions = (
                       ("read_teacher", "Can read teacher"), 
                       )
        
class Student(models.Model):
    name = models.CharField(max_length=50)
    grade = models.IntegerField(blank=False, null=False)
    create_time = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    update_time = models.DateTimeField(auto_now = True, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student'
        permissions = (
                       ("read_student", "Can read student"), 
                       )

class Mark(models.Model):
    score = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add = True, blank=True, null=True)
    update_time = models.DateTimeField(auto_now = True, blank=True, null=True)
    subject = models.ForeignKey(Subject)
    student = models.ForeignKey(Student)
        
    class Meta:
        db_table = 'marks'
        unique_together = ('subject', 'student',)
        permissions = (
                       ("read_marks", "Can read marks"), 
                       )
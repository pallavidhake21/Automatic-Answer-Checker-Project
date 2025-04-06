from django.db import models

# Create your models here.

class Exam(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Corrans = models.CharField(max_length=100)

    def __str__(self):
        return self.Question


class Registration(models.Model):
    Fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    choice = models.CharField(max_length=100,null=True)
    Gender = models.CharField(max_length=10)
    number = models.IntegerField()
    Address = models.CharField(max_length=15)

    def __str__(self):
        return self.Fname

class Answer(models.Model):
    ans = models.CharField(max_length=100)
from django.db import models

# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length = 50)

class Student(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    address = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 15)
    education = models.CharField(max_length = 10)
    major = models.CharField(max_length = 100)
    subscription = models.ManyToManyField(Specialization)

class Classroom(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    batch_name = models.CharField(max_length = 20)
    day_night_status = models.IntegerField()
    online_status = models.CharField(max_length = 10)

class Score(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    course_name = models.CharField(max_length = 50)
    score = models.IntegerField()




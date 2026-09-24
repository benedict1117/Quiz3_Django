from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length= 30)
    year_level = models.IntegerField(default= 1)
    section = models.CharField(max_length= 20)

    def __str__(self):
        return self.name
# Create your models here.

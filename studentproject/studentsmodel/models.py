from django.db import models

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

# Create your models here.
class Student(models.Model):
    name = models.CharField('Student Name', max_length=128)
    age = models.PositiveIntegerField(default=10)
    gender = models.CharField(max_length=8, choices=GENDER)
    picture = models.ImageField(upload_to='media/')
    fees = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name


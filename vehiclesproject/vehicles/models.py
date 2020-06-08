from django.db import models

BRANDS = (
    ('HN','HONDA'),
    ('TY','Toyota'),
    ('MD','Mercedes'),
    ('BMW','BMW'),
)


# Create your models here.
class Vehicle(models.Model):
    registration_number = models.CharField('Vehicle Registration Number', max_length=16)
    color = models.CharField(max_length=128)
    model = models.CharField(max_length=64)
    brand = models.CharField(max_length=16,choices=BRANDS)
    image = models.ImageField('Vehicle Image', upload_to='media/')
    menufectured_date = models.DateField('Menufectured Date',auto_now_add=True)

    def __str__(self):
        return self.registration_number +' ' + self.model
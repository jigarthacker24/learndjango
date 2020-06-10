from django.db import models

# Create your models here.
class PizzaModel(models.Model):
    name = models.CharField(max_length=10)
    price = models.CharField(max_length=10)

def __str__(self):
    return self.name


class CustomerModel(models.Model):
    userid = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)

class OrderModel(models.Model):
    username=models.CharField(max_length=10)
    phoneno=models.CharField(max_length=10)
    address=models.CharField(max_length=10)
    ordereditems=models.CharField(max_length=100)
    status = models.CharField(max_length=10)
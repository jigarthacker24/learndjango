from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField('Book Title',max_length=128)
    author = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + 'by' + self.author

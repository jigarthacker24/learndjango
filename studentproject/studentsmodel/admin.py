from django.contrib import admin
from studentsmodel.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','age','gender','picture','fees']

admin.site.register(Student,StudentAdmin)

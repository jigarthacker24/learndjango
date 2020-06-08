from django.shortcuts import render
from django.http import HttpResponse
from studentsmodel.models import Student

# Create your views here.

def index(request):
    obj_list = Student.objects.all()
    return render(request,'index.html',{'students':obj_list})

def login(request):
    return HttpResponse("<pre>Learning Django views from HTTP Response.</pre>")

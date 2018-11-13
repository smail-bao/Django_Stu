from django.shortcuts import render
from app01 import models
# Create your views here.

def students(request):
    stu_obj = models.Students.objects.all()
    return render(request,'get_students.html',{'stu_obj':stu_obj})
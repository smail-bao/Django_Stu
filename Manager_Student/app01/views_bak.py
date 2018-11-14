from django.shortcuts import render,redirect
from app01 import models
# Create your views here.

def students(request):
    if request.method == "GET":
        stu_obj = models.Students.objects.all()
        class_obj = models.Classes.objects.all()
        # class_id = list(zip(*class_obj))
        return render(request,'get_students.html',{'stu_obj':stu_obj,'class_obj':class_obj})
    elif request.method == "POST":
        username = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        classes = request.POST.get('classes')
        models.Students.objects.create(
            name=username,
            age=age,
            gender=gender,
            cs_id=classes
        )
        return redirect('students.html')

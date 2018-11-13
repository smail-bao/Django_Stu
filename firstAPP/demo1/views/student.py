from django.shortcuts import render,redirect,HttpResponse
from demo1 import models

def get_student(request):
    student_list=models.Students.objects.all()
    return render(request,'get_student.html',{'student_list':student_list})

def add_student(request):
    if request.method == 'GET':
        classes_list = models.Classes.objects.all()
        return render(request,'add_student.html',{'classes_list':classes_list})
    elif request.method == 'POST':
        # name = models.CharField(max_length=32)
        # age = models.IntegerField()
        # gender = models.BooleanField()
        # cs = models.ForeignKey(Classes, on_delete=models.CASCADE)
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        cs_id=request.POST.get('classes')
        # print(name,age,gender,cs_id)
        models.Students.objects.create(
            name=name,
            age=age,
            gender=gender,
            cs_id=cs_id
        )
        return redirect('student.html')

def edit_student(request):
    if request.method == 'GET':
        nid=request.GET.get('nid')
        classes_list = models.Classes.objects.all()
        # classes_list = models.Classes.objects.values('id','title') 这里我们用values更好，classes_list 是一个类列表（QuerySet）里包含多个字典
        obj=models.Students.objects.filter(id=nid).first()
        return render(request,'edit_student.html',{'obj':obj,'classes_list':classes_list})
    elif request.method == 'POST':
        nid=request.POST.get('nid')
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        cs_id=request.POST.get('classes')
        print(59*'=')
        print(nid)
        print(59 * '=')
        models.Students.objects.filter(id=nid).update(
            name=name,
            age=age,
            gender=gender,
            cs_id=cs_id
        )
        return redirect('student.html')

def del_student(request):
    nid=request.GET.get('nid')
    models.Students.objects.filter(id=nid).delete()
    return redirect('student.html')

from django.shortcuts import render,redirect,HttpResponse
from app01 import models
import json
# Create your views here.

def students(request):
    stu_obj = models.Students.objects.all()
    class_obj = models.Classes.objects.all()
    # class_id = list(zip(*class_obj))
    return render(request,'get_students.html',{'stu_obj':stu_obj,'class_obj':class_obj})

def add_student(request):
    response = {'status':True,'msg':None}
    try:
        username=request.POST.get('username')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        cls_id=request.POST.get('cls_id')
        models.Students.objects.create(
            name=username,
            age=age,
            gender=gender,
            cs_id=cls_id
        )
    except Exception as e:
        response['status'] = False
        response['msg'] = '用户输入有误'
    # 因为这里前端HttpResponse 返回的是字符串，但是这里是字典，所以需要应用json.dumps
    res = json.dumps(response,ensure_ascii=False)
    print(res,type(res))
    return HttpResponse(res)

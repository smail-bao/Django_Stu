from django.shortcuts import render, redirect, HttpResponse
from app01 import models
import json


# Create your views here.

def students(request):
    stu_obj = models.Students.objects.all()
    class_obj = models.Classes.objects.all()
    # class_id = list(zip(*class_obj))
    return render(request, 'get_students.html', {'stu_obj': stu_obj, 'class_obj': class_obj})


def add_student(request):
    response = {'status': True, 'msg': None}
    try:
        username = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cls_id = request.POST.get('cls_id')
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
    res = json.dumps(response, ensure_ascii=False)
    print(res, type(res))
    return HttpResponse(res)


def del_student(request):
    response = {'status': True}
    try:
        nid = request.GET.get('nid')
        models.Students.objects.filter(id=nid).delete()
    except Exception as e:
        response['status'] = False
    return HttpResponse(json.dumps(response, ensure_ascii=False))

def edit_student(request):
    response = {'code':200,'msg':None}
    try:
        nid = request.GET.get('nid')
        name = request.GET.get('username')
        age = request.GET.get('age')
        gender = request.GET.get('gender')
        cls_id = request.GET.get('cls_id')
        models.Students.objects.filter(id=nid).update(
            name=name,
            age=age,
            gender=gender,
            cs_id=cls_id
        )
    except Exception as e:
        response['code']=500
        response['msg']=e
    return HttpResponse(json.dumps(response,ensure_ascii=False))
from django.shortcuts import render,HttpResponse,redirect
from demo1 import models

def index(request):
    return render(request,'index.html')

def get_classes(request):
    class_list=models.Classes.objects.all()
    return render(request,'get_classes.html',{'class_list':class_list})

def add_classes(request):
    if request.method == "GET":
        return render(request,'add_classes.html')
    elif request.method == "POST":
        title=request.POST.get('title')
        models.Classes.objects.create(title=title)
        return redirect('classes.html')

def del_classes(request):
    nid=request.GET.get('nid')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('classes.html')

def edit_classes(request):
    if request.method=='GET':
        nid=request.GET.get('nid')
        obj=models.Classes.objects.filter(id=nid).first()
        return render(request,'edit_classes.html',{'obj':obj})
    elif request.method=='POST':
        nid=request.GET.get('nid')   # 这个nid 是放在url里的是GET请求
        title=request.POST.get('title')
        models.Classes.objects.filter(id=nid).update(title=title)
        return redirect('classes.html')

def dispatch_teacher(request):
    if request.method=='GET':
        nid=request.GET.get('nid')
        cls_obj = models.Classes.objects.filter(id=nid).first()
        # cls_teacher_list = cls_obj.m.all()
        cls_teacher_list = cls_obj.m.values_list('id','name')
        # cls_teacher_list 得到的结果是这样的[(1,'alex'),(2,'egon'),(3,'yuanhao')]
        teacher_id_list = list(zip(*cls_teacher_list))[0]
        # zip 函数可以接收任意多个可迭代对象作为参数，将对象中对应的元素打包成一个元祖，然后返回一个可迭代的zip对象
        # cls_teacher_id_list得到的结果是(1,2,3)
        all_teacher_list = models.Teachers.objects.all()
        # for i in all_teacher_list:
        #     print(i.id,i.name)

        return render(request,
                      'dispatch_teacher.html',
                      {'cls_obj':cls_obj,
                       'teacher_id_list':teacher_id_list,
                       'all_teacher_list':all_teacher_list,
                       'nid':nid
                       }
                      )
    elif request.method == 'POST':
        nid=request.GET.get('nid')
        sel_teacher_id_list=request.POST.getlist("teacher_id")
        obj=models.Classes.objects.filter(id=nid).first()
        obj.m.set(sel_teacher_id_list)
        return redirect('classes.html')
'''
还有一种方案就是我们在classes.html 添加一列，任课老师，我们对classes遍历
obj=modles.Classes.objects.filter(id=1).m.all()  这个拿到的就是任课老师的对象信息，我们可以进行遍历，拿到for i in obj ,取值i.name
'''
from django.shortcuts import render,HttpResponse

def ajax1(request):
    return render(request,'ajax1.html')

def ajax2(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    import time
    time.sleep(3)
    return HttpResponse('Hello World')
def ajax3(request):
    v1=request.POST.get('v1')
    v2=request.POST.get('v2')
    try:
        v3=int(v1)+int(v2)
    except Exception as e:
        v3="输入格式有误"
    return HttpResponse(v3)



'''
我们在select的时候我们代码选择的话用

$('#sel').val(2)         单选
$('#sel').val([1,3,5])   多选，同时在select标签添加multiple
'''
from django.db import models

# Create your models here.
'''
老师表和班级表是多对多的关系
一个老师可以带多个班级
一个班级也有可能有多个老师
所以这里需要第三张表来存放两者的关系
'''

class Classes(models.Model):
    '''
    班级表
    '''
    title=models.CharField(max_length=32)
    m = models.ManyToManyField("Teachers")

'''
这里我们执行
obj=Classes.objects.filter(title='Java 1 班').first()
obj.id
obj.title
ret = obj.m.all()
这个ret 包含了“Java 1 班”班级信息，老师信息，以及班级和老师的关系
'''

class Teachers(models.Model):
    '''
    老师表
    '''
    name=models.CharField(max_length=32)

class Students(models.Model):
    '''
    学生表
    cs 表示 班级和学生的关系,外键
    BooleanField 只能填 True  Flase
    '''
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    gender=models.BooleanField()
    cs=models.ForeignKey(Classes,on_delete=models.CASCADE)
    '''
    这里cs 表示的是一个对象，也就是数据库中的Classes的表的所有字段
    但是这里我们要是增加数据的话，我们要这样
    Students.objects.create(name='xxx',age=12,gender=1,cs_id=3)
    或者
    Students.objects.create(name='xxx',age=12,gender=1,cs=Classes.objects.filter(id=1).first())
    '''

    '''
    class C2T(models.Model):
        cid=models.IntegerField(Classes)
        tid=models.IntegerField(Teachers)
    cid(只能是class表中的数据)  --->  class_id
    tid（只能是teacher表中的数据）  --->  teacher_id
    这个第三种表不用我们自己创建，我们使用ORM中的ManayToManayField属性
    这个随便加在那个类中，这里我们加在Classes类中
    models.ManyToManyField("Teachers")
    这里我们要用双引号括起来是因为Teacher在下面，他找不到，这里我们用双引号就好了
    '''

'''
1 类代表数据库表
2 类的对象代指数据库的一行记录
3 外键字段代表关联表的一行数据（类的对象）
4 ManayToManay 字段会生成第三张表，依赖关联表对第三张表间接操作

实例
拿到所有学生的姓名以及所在班级的名称
方式1
stu_list = Student.objects.all()   这个返回的是一个QuerySet 对象（类列表，列表里套着对象）
for row in stu_list:
    row.name,row.cs.title
方式2
stu_list = Student.objects.all().values("name","cs.title")这个返回的就是一个列表里套着字典
[{'name':'bigbao','cs.title':'python'},{'name':'hu','cs.title':'java'}]

找到三班所有学生
Students.objects.filter(cs__title='三班')

正向的跨表查询这里我们用双下划线 __
反向跨表查询 类名小写_set，这个下面有.all   .get等方法

比如这里我们的Student 有一个外键 cs 字段关联Classes
我们通过cs 字段可以查看Classes的相关信息
但是我们也可以通过Classes去查找Students表的相关信息（这个就是反向查询了）
obj=models.Classes.objects.filter(title='Python2班').first() 这个得到的是一个querySet对象
这个时候我们怎么去查Python2班的所有学生，这个时候我们就需要去反向查询，方法为
obj.students_set.all()   ---->这个时候我们就拿到了querySet的集合了（这里我们认为Classes表隐藏了一个students_set字段，但是这里Students表得存在一个外键）
这里我们也可以修改Students表的外键字段，添加一个属性 related_name='xxx'
那么那个隐藏字段我们就可以用 xxx 来表示了，而可以不用“类名小写_set”了
'''

'''
接下来学习多对多
多对多查找
cls_obj=Classes.objects.all()
for obj in cls_obj:
    print(obj.title,cls_obj.m.all()) 取到的是班级信息和querySet对象
    for row in obj.m.all():
        print(row.name) 这样就取到了老师的姓名了，总和上面的for循环我们可以拿到obj.title  row.name 这样我们就知道班级的任课老师有哪些了
这里我们可以用m__name 去获得老师名字（跨表操作）

正向添加
obj=Classes.objects.filter(id=1).first()
obj.m.add(3)  这样就给第三张表加了一个对应关系,就是给班级id为1的增加一个id为3的老师

反向添加
obj=models.Teachers.filter(id=2).first()
obj.classes_set.add(2)
这个就是给id为2的老师增加一个id为2的班级，这里Teachers没有m2m的关系字段，所以只有通过反向关系，表名小写_set去操作了

练习：给班级分配老师

'''

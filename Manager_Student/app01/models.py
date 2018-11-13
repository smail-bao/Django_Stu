from django.db import models

# Create your models here.

class Classes(models.Model):
    '''
    班级表
    '''
    title=models.CharField(max_length=32)
    m = models.ManyToManyField("Teachers")

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


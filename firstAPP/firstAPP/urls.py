"""firstAPP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demo1.views import classes
from demo1.views import student
from demo1.views import ajax



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html',classes.index),
    path('classes.html',classes.get_classes),
    path('add_classes.html',classes.add_classes),
    path('del_classes.html',classes.del_classes),
    path('edit_classes.html',classes.edit_classes),
    path('dispatch_teacher.html',classes.dispatch_teacher),

    path('student.html',student.get_student),
    path('add_student.html',student.add_student),
    path('edit_student.html',student.edit_student),
    path('del_student.html',student.del_student),
    path('ajax1.html',ajax.ajax1),
    path('ajax2.html',ajax.ajax2),
    path('ajax3.html',ajax.ajax3),
]

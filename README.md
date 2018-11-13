创建project的流程
1、Pycharm创建一个Django项目，添加一个app应用
2、静态文件配置 STATICFILES_DIR=(os.path.join(BASE_DIR,'static'))  
3、app注册   settings.py---INSTALLED_APPS-->'appname'
4、模板路径创建 settings.py--->TEMPLATES--->'DIRS': [os.path.join(BASE_DIR,'templates')],

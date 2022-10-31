# 明日方舟wiki后端程序

创建项目
```shell
django-admin startproject mysite
```

启动服务  
```shell
python manage.py runserver 0:8000
```

创建应用
```shell
python manage.py startapp polls
```

数据库相关
```shell
# 模型数据迁移
python manage.py makemigrations polls

# 查看数据库迁移SQL
python manage.py sqlmigrate polls 0001

# 创建数据表
python manage.py migrate
```

后台管理
```shell
# 访问地址
http://127.0.0.1:8000/admin/  admin/admin

```
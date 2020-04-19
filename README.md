# CHINSLICKING项目


## 安装
```
pip3 install pipenv
pipenv shell
pipenv install django
pipenv install pymysql
pipenv install pillow
pipenv install pymysql
pipenv install django-simpleui
```

## 添加环境变量
```
export MYSQL_HOST=localhost
export MYSQL_PORT=3306
export MYSQL_USER=user
export MYSQL_PASS=password
export DJANGO_SETTINGS_PROFILE=pro
export SECRET_KEY='pz0_7d@n$!xc$o5c4d-8k@*-#=z-%5^ip=uct(&0tyr4tv)qyx'
```


## 部署（centos7+python3.7+django2.2.1+uwsgi）
```
pipenv shell
uwsgi --ini chinslickingweb_uwsgi.ini
uwsgi --reload chinslickingweb_uwsgi.ini
uwsgi --stop uwsgi.pid
```




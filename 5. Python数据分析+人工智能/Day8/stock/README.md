# stock
## 运行环境建立
### 运行环境建立(生成migrate环境)
    $ python3 manage.py makemigrations
#### 错误的解决方法
 - django.db.utils.InternalError: (1049, "Unknown database 'stockplus_db'") 错误
    -  $ mysql -uroot -p123456
       mysql> create database stockplus_db  default  charset utf8;
 - ImportError: No module named 'tushare' # 错误
     - $ sudo pip3 install tushare
 - Cannot uninstall 'pyzmq'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall. 错误
     - 删除pyzmq
     - $ sudo pip3 install tushare --ignore-installed pyzmq

### 进行创建数据表
    $ python3 manage.py migrate

### 运行python项目
    $ python3 manage.py runserver 0.0.0.0:8004

### web浏览器查看
    http://localhost:8004/index-1


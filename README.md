# flask-framework
flask 高并发集群框架

##nginx配置
```server {
        listen 80;
        server_name '你的域名';
        location / {
	        include uwsgi_params;
	         uwsgi_pass unix:/home/flask-framework/uwsgi.sock;
	         uwsgi_param UWSGI_CHDIR  /home/flask-framework/;
	         uwsgi_param UWSGI_SCRIPT run; ### myapp.py app文件名称
	         access_log /home/flask-framework/app_access.log;
        }
    }```
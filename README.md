#nginx配置
```
server {
        listen 80;
        server_name '你的域名';
        location / {
	        include uwsgi_params;
	         uwsgi_pass unix:/home/flask-framework/uwsgi.sock;
	         uwsgi_param UWSGI_CHDIR  /home/flask-framework/;
	         uwsgi_param UWSGI_SCRIPT run; ### myapp.py app文件名称
	         access_log /home/flask-framework/app_access.log;
        }
    }
```

jwt的包使用的是 pyjwt
为避免干扰请 卸载jwt python_jwt flask_jwt等包

读后有收获可以微信请作者喝咖啡：:kissing_heart:

<img src="https://shubei-app.oss-cn-beijing.aliyuncs.com/ItisDLWeiXinShou.jpg" width="30%">

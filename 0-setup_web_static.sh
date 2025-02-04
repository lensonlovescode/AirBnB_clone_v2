#!/usr/bin/env bash
#A Bash script that sets up my web servers for the deployment of web_static

sudo apt install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo -e "Testing..." | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
configuration="server {

        listen 80 default_server;
        listen [::]:80 default_server;

        server_name lensonmutugi.tech;

        add_header X-Served-By $(hostname);

        location / {
                root /var/www/html;
        }

        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=dQw4w9WgXcQ;
        }

        location /hbnb_static {
                alias /data/web_static/current/;
        }

        location ~ /\.ht {
               deny all;
        }

        error_page 404 /ERROR404.html;
}"
echo "$configuration" | sudo tee /etc/nginx/sites-available/default > /dev/null
sudo service nginx restart

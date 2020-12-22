#!/usr/bin/env bash
# sets up your web servers for the deployment of web_stat

# install ngnix if not exists
sudo apt-get -y update
sudo apt-get -y install nginx

# Create directories if not exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Create fake HTML with simple content" > /data/web_static/releases/test/index.html

# create symbolic link (remove if the link exists)
ln -sf /data/web_static/releases/test/ /data/web_static/current

# set permision
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

# config default file
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://www.holbertonschool.com/;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

sudo /usr/sbin/service nginx restart

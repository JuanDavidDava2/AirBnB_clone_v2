#!/usr/bin/env bash
# This script configure a server with some specifications


# Setup file directory system for webstatic files
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo echo "<h1>This is my code<h1>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Standar 404 message
sudo mkdir -p /var/www/html/
sudo echo "Holberton School for the win!" | sudo tee /var/www/html/index.html

# Install nginx web server
sudo apt-get update
sudo apt-get install -y nginx

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=DHITmcKUGik;
    }
    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}" > /etc/nginx/sites-available/default

sudo service nginx restart

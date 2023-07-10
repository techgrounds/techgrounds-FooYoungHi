#!/bin/bash
# Install Apache Web Server and PHP
yum install -y httpd php
# Turn on web server
chkconfig httpd on
service httpd start
touch /var/www/html/healthcheck.php #needed for the health check, do not remove

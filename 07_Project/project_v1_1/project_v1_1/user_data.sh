#!/bin/bash
# Install Apache Web Server, PHP, and MariaDB
yum update -y
yum upgrade -y
yum install -y httpd php mariadb
# Turn on web server
chkconfig httpd on
service httpd start
cat > /var/www/html/index.php "Het Werkt" # Create a file on the root to make the health checks work.
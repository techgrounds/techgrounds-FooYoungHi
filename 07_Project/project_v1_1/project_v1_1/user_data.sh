#!/bin/bash
# Install Apache Web Server, PHP, and MariaDB
yum update -y
yum upgrade -y
yum install -y httpd php mariadb
# Download Lab files
wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
unzip lab-app.zip -d /var/www/html/
# Turn on web server
chkconfig httpd on
service httpd start
#cat > /var/www/html/index.php "Het Werkt" # Create a file on the root to make the health checks work.
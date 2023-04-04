apt update -y

apt install apache2 -y

systemctl start apache2

systemctl enable apache2

systemctl status apache2 --no-pager --full

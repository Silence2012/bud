ROOT_PASSWORD=moon_123
echo "root:$ROOT_PASSWORD" |chpasswd
echo root password:$ROOT_PASSWORD
service ssh start
nohup moon > /var/log/moon_start.log 2>&1 &
exec /bin/bash $@

FROM letv:centos6
MAINTAINER sunxiaoning@letv.com
#Date: 2015.4
#Desc: 
EXPOSE 8888
ADD ./dist/moon-0.1.5_dev-1.noarch.rpm /tmp/
ADD start.sh /root/
RUN yum install /tmp/moon-0.1.5_dev-1.noarch.rpm -y
ENTRYPOINT ["/bin/bash","/root/start.sh"]

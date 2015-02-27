from docker import Client
c = Client()
#r = c.create_container(image="letv:centos6",stdin_open=True,tty=True,command="/bin/bash -d",ports=[80,22],name="dboy-3")
#print str(r)
con_list = []
for con in c.containers():
    con_list.append(con[u'Id'])
print con_list

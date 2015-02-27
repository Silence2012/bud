import subprocess
def read_ifconfig():
    p = subprocess.Popen('ip netns exec 3d3654cdad0a434d16a51c6a9fcb2a8b7410442c07412f2de2a5530675096bc0 ifconfig',stdout=subprocess.PIPE,shell=True)
    return p.communicate()[0]
ret = read_ifconfig()
data =  (i for i in ret.split('\n\n') if i and not i.startswith('lo'))
for i in data:
    print i
    print "=================\n"


README<br>
=====
2015.3.13
1.GET http://$IP:8888/v1                  return all arguments of the running containers on this host
2.GET http://$IP:8888/v1/runContainerId    return the Id value of the running containers
3.GET http://$IP:8888/v1/getArg            return  the 'Config' option of the running containers
4.GET http://$IP:8888/v1/container/cpu   return the cpu metrics  of the containers 
5.GET http://$IP:8888/v1/container/mem   retrun the memory metrics of the containers
6.GET http://$IP:8888/v1/container/blkio return the blkio metrics of the containers
7.GET http://$IP:8888/v1/container/net   return the net metrics of the containers
#agent 0.1.1 rc1<br>

##1.scrape the metric of the cpuacct mem blkio netstat<br>
#agent 0.1.2 rc1<br>
##1.add memconfig blkio io_queued<br>


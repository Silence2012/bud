README<br>
=====
2015.3.13
v1/container/metrics	 返回节点上所有container的 metrics
v1/container/cpu	返回节点上所有container的cpu的metrics
v1/container/${container id}/cpu	返回节点上指定container id的cpu的metrics
v1/container/mem	返回节点上所有container的mem的metrics
v1/container/${container id}/mem	返回节点上指定container id的mem的metrics
v1/container/blkio	返回节点上所有container的blkio的metrics
v1/container/${container id}/blkio	返回节点上指定container id的blkio的metrics
v1/container/net	返回节点上所有container的net的metrics
v1/container/${container id}/net	返回节点上指定container id的net的metrics
v1/host/cpu	返回host节点上的cpu的metrics
v1/host/mem	返回host节点上的mem的metrics
v1/host/net	返回host节点上的net的metrics
v1/host/disk	返回host节点上的disk的metrics
v1/containers	返回节点上所有的container id
v1/container/${container id}/arg	返回节点上指定container id 的配置参数
#agent 0.1.1 rc1<br>

##1.scrape the metric of the cpuacct mem blkio netstat<br>
#agent 0.1.2 rc1<br>
##1.add memconfig blkio io_queued<br>


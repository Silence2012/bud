#!/usr/bin/env python
import re
import os
from docker import Client
class ContainerMetric(object):
    def __init__(self,containerID):
       self.containerID = containerID
	def display_cpu(*cpuArg):
	     
  

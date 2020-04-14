#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ding_topo.py
@Time    :   2019/11/08 08:22:02
@Author  :   Paul Yu 
@Contact :   13186576376@163.com
@Github  :   https://github.com/nicePaul521/Ryu.git
'''

# here put the import lib

from mininet.net import Mininet                                                                                                                                      
from mininet.log import setLogLevel       
from mininet.cli import CLI  
from mininet.topo import Topo
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.node import RemoteController 

"""

"""

class mytopo(Topo):
    def __init__(self,**opts):
        super(mytopo,self).__init__()

        #add switches
        nS = 8
        s = [self.addSwitch('s%d' % i) for i in range(1,nS+1)]

        #add hosts
        nH = 6
        h = [self.addHost('h%d' % i,mac = '00:00:00:00:00:0%d' % i,cpu=.5/nH) for i in range(1,nH+1)]

        linkopt1 = dict(bw=100,delay='3ms', loss=3,max_queue_size=1000,use_htb=True)
        linkopt2 = dict(bw=100,delay='6ms',loss=6,max_queue_size=1000,use_htb=True)
        linkopt3 = dict(bw=100,delay='9ms',loss=9,max_queue_size=1000,use_htb=True)
        linkopt4 = dict(bw=100,delay='12ms',loss=12,max_queue_size=1000,use_htb=True)
        linkopt5 = dict(bw=100,delay='15ms',loss=15,max_queue_size=1000,use_htb=True)

        self.addLink(h[0],s[0])
        self.addLink(h[1],s[0])
        self.addLink(h[2],s[0])
        self.addLink(h[3],s[0])
        self.addLink(h[4],s[0])
        self.addLink(s[0],s[1])
        self.addLink(s[1],s[2],**linkopt1)
        self.addLink(s[1],s[3],**linkopt2)
        self.addLink(s[1],s[4],**linkopt3)
        self.addLink(s[1],s[5],**linkopt4)
        self.addLink(s[1],s[6],**linkopt5)
        self.addLink(s[2],s[7],**linkopt1)
        self.addLink(s[3],s[7],**linkopt2)
        self.addLink(s[4],s[7],**linkopt3)
        self.addLink(s[5],s[7],**linkopt4)
        self.addLink(s[6],s[7],**linkopt5)
        self.addLink(h[5],s[7])

if __name__ == '__main__': 
    setLogLevel( 'info' )                                                                              
    net = Mininet(topo=mytopo(),host=CPULimitedHost,link=TCLink,controller=RemoteController('ryuController'))                                  
    net.start()
    #net.iperf()
    "output host-port"
    dumpNodeConnections(net.hosts)
    "output results of bradwidth between nodes"
    
    "run GUI to show xterm"
    # app = ConsoleApp( net, width=10 ) 
    # app.mainloop()
    "show CLI recommand"        
    CLI(net)                                                                                                                                                                
    net.stop()      
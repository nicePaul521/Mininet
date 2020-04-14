#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ryu.py
@Time    :   2019/10/12 10:25:32
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
#from consoles import ConsoleApp                                                    
                                                                                                       
class QosTopo(Topo):
    def __init__(self,**opts):
        super(QosTopo,self).__init__()

        #add switches
        nS = 6
        s = [self.addSwitch('s%d' % i) for i in range(1,nS+1)]

        #add h
        nH = 4
        h = [self.addHost('h%d' % i,mac = '00:00:00:00:00:0%d' % i,cpu=.5/nH) for i in range(1,nH+1)]

        #add links
        '''
           h1    S2----S5   h3
             \  /     /  \ /
              S1-----S3---S6
             /  \   /    / \
           h2    S4------   h4
        '''  
        linkopt0 = dict(bw=10, delay='3ms')# host <---> switch
        linkopt1 = dict(bw=60, delay='5ms', loss=3, max_queue_size=1000, use_htb=True)# good Qos Link
        linkopt2 = dict(bw=100, delay='9ms', loss=6, max_queue_size=1000, use_htb=True)# bad Qos Link
    
        self.addLink(h[0],s[0])#h1---s1
        self.addLink(h[1],s[0])#h2---s1
        self.addLink(s[0],s[1],**linkopt2)#s1---s2
        self.addLink(s[0],s[2],**linkopt2)#s1---s3
        self.addLink(s[0],s[3])#s1---s4
        self.addLink(s[1],s[4])#s2---s5
        self.addLink(s[2],s[4])#s3---s5
        self.addLink(s[2],s[5],**linkopt1)#s3---s6
        self.addLink(s[2],s[3])#s3---s4
        self.addLink(s[4],s[5])#s5---s6
        self.addLink(s[3],s[5],**linkopt2)#s4---s6
        self.addLink(h[2],s[5])#s6---h3
        self.addLink(h[3],s[5])#s6---h4
#topos = {'mytopo':(lambda:QosTopo())}
                                                                                                       
if __name__ == '__main__':                                                                             
    setLogLevel( 'info' )                                                                              
    net = Mininet(topo=QosTopo(),host=CPULimitedHost,link=TCLink,controller=RemoteController('paulController'))                                  
    net.start()
    #net.iperf()
    "output host-port"
    # dumpNodeConnections(net.h)
    "output results of bradwidth between nodes"
    # h1,h2 = net.get('h1','h2')
    # print "testing bandwidth between h1 and h2" 
    # net.iperf((h1,h2))
    "run GUI to show xterm"
    # app = ConsoleApp( net, width=10 ) 
    # app.mainloop()
    "show CLI recommand"        
    CLI(net)                                                                                                                                                                
    net.stop()      
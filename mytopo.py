#!/usr/bin/python  
#-*- coding:utf-8 -*-
import re  
import sys  
from mininet.cli import CLI  
from mininet.log import setLogLevel, info, error  
from mininet.net import Mininet  
from mininet.link import Intf  
from mininet.util import quietRun  
from mininet.node import OVSSwitch, OVSController, Controller, RemoteController  
from mininet.topo import Topo  
  
class MyTopo( Topo ):  
#    "this topo is used for Scheme_1"  
      
    def __init__( self ):  
        "Create custom topo."  
  
        # Initialize topology  
        Topo.__init__( self )  
  
        # Add hosts   
        h1 = self.addHost( 'h1' , ip="10.0.0.1/24", mac="00:00:00:00:00:01")  
        h2 = self.addHost( 'h2' , ip="10.0.0.2/24", mac="00:00:00:00:00:02")  
        h3 = self.addHost( 'h3' , ip="10.0.0.3/24", mac="00:00:00:00:00:03")
        h4 = self.addHost( 'h4' , ip="10.0.0.4/24", mac="00:00:00:00:00:04")
          
        # Add switches  
        s1 = self.addSwitch( 's1' )  
        # s2 = self.addSwitch( 's2' )  
        # s3 = self.addSwitch( 's3' )  
  
        # Add links  
        # self.addLink( s1, s2 )  
        # self.addLink( s2, s3 )  
        self.addLink( s1, h1 )
        self.addLink( s1, h2 )  
        self.addLink( s1, h3 ) 
        self.addLink( s1, h4 ) 
  
if __name__ == '__main__':  
    setLogLevel( 'info' )  
    info( '*** Creating network\n' )  
    net = Mininet( topo=MyTopo(),controller=None) #关键函数，创建mininet网络，指定拓扑和控制器。这里的控制器在后面添加进去  
    c0 = RemoteController( 'c0', ip='127.0.0.1', port=6633 )  
    net.addController(c0)  
    net.start()  
    CLI( net )  
    net.stop()  
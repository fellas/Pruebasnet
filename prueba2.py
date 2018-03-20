#!/usr/bin/python

"""
This example shows how to add an interface (for example a real
hardware interface) to a network after the network is created.
"""

import re

from mininet.cli import CLI
from mininet.log import setLogLevel, info, error
from mininet.net import Mininet
from mininet.link import Intf
from mininet.topolib import TreeTopo
from mininet.util import quietRun

def checkIntf( intf ):
    "Make sure intf exists and is not configured."
    if ( ' %s:' % intf ) not in quietRun( 'ip link show' ):
        error( 'Error:', intf, 'does not exist!\n' )
        exit( 1 )
    ips = re.findall( r'\d+\.\d+\.\d+\.\d+', quietRun( 'ifconfig ' + intf ) )
    if ips:
        error( 'Error:', intf, 'has an IP address,'
               'and is probably in use!\n' )
        exit( 1 )
class SimplePktSwitch(Topo):
    """Simple topology example."""


    def __init__(self, **opts):
        """Create custom topo."""

        # Initialize topology
        # It uses the constructor for the Topo cloass
        super(SimplePktSwitch, self).__init__(**opts)

        # Add hosts and switches
        #h1 = self.addHost('h1')
        #h2 = self.addHost('h2')


        # Adding switches
        s1 = self.addSwitch('s1', dpid="0000000000000001")
        s2 = self.addSwitch('s2', dpid="0000000000000002")
        s3 = self.addSwitch('s3', dpid="0000000000000003")
        s4 = self.addSwitch('s4', dpid="0000000000000004")
	    s5 = self.addSwitch('s5', dpid="0000000000000005")
		self.addLink(s1, s2)
		self.addLink(s1, s3)
		self.addLink(s1, s4)
		self.addLink(s2, s5)
		self.addLink(s3, s5)
		self.addLink(s4, s5)
def run():
	intfName = 'eth1'
    info( '*** Checking', intfName, '\n' )
    checkIntf( intfName )
	intfName1 = 'eth2'
    info( '*** Checking', intfName, '\n' )
    checkIntf( intfName1 )
    c = RemoteController('c', '127.0.0.1', 6633)
    OVSSwitch13 = partial( OVSSwitch, protocols='OpenFlow13' )
    net = Mininet(topo=SimplePktSwitch(),switch=OVSSwitch13, controller=None)
    net.addController(c)
	switch = net.switches[ 0 ]
    info( '*** Adding hardware interface', intfName, 'to switch',
          switch.name, '\n' )
    _intf = Intf( intfName, node=switch )
	switch1 = net.switches[ 4 ]
    info( '*** Adding hardware interface', intfName, 'to switch',
          switch.name, '\n' )
    _intf = Intf( intfName1, node=switch1 )
    net.start()

    CLI(net)
    net.stop()
if __name__ == '__main__':
    setLogLevel('info')
    run()
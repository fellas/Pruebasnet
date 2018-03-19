__author__ = 'Ehsan'
from mininet.node import CPULimitedHost, Host
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.nodelib import LinuxBridge
from mininet.log import setLogLevel, info
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.link import TCLink, Intf
from functools import partial

"""
Instructions to run the topo:
    1. Go to directory where this fil is.
    2. run: sudo -E python Simple_Pkt_Topo.py.py
The topo has 4 switches and 4 hosts. They are connected in a star shape.
"""

def checkIntf( intf ):
	#Make sure intf exists and is not configured.
	if ( ' %s:' % intf ) not in quietRun( 'ip link show' ):
		error( 'Error:', intf, 'does not exist!\n' )
		exit( 1 )
	ips = re.findall( r'\d+\.\d+\.\d+\.\d+', quietRun( 'ifconfig ' + intf ) )
	if ips:
		error( 'Error:', intf, 'has an IP address, and is probably in use!' )
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
		# agregar link
		info( '\n*** Creating Physical Interfaces ***\n' )
		info( '	*** Checking', 'eth0', '\n' )
		checkIntf( 'eth1' )
		eth0 = Intf( 'eth0' , node=s1 )
		info( '\n*** Creating Physical Interfaces ***\n' )
		info( '	*** Checking', 'eth1', '\n' )
		checkIntf( 'eth2' )
		eth0 = Intf( 'eth2' , node=s5 )
        # Add links
        self.addLink(h1, s1)
	#self.addLink(s1, s2)
	self.addLink(s1, s3)
	self.addLink(s1, s4)
	self.addLink(s2, s5)
	self.addLink(s3, s5)
	self.addLink(s4, s5)
	#self.addLink(s5, h2)


def run():
    c = RemoteController('c', '127.0.0.1', 6633)
    OVSSwitch13 = partial( OVSSwitch, protocols='OpenFlow13' )
    net = Mininet(topo=SimplePktSwitch(),switch=OVSSwitch13, controller=None)
    net.addController(c)
    net.start()

    CLI(net)
    net.stop()

# if the script is run directly (sudo custom/optical.py):
if __name__ == '__main__':
    setLogLevel('info')
    run()

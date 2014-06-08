#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import irange, dumpNodeConnections
from mininet.log import setLogLevel

class CustomTopo(Topo):

    def __init__(self, linkopts1=1, linkopts2=2, linkopts3=2, fanout=2, **opts):
        # Initialize topology and default options
        super(CustomTopo, self).__init__(**opts)

        # Add your logic here ...
        linkopts = dict(bw = 10, delay = '5ms', loss = 1, max_queue_size = 1000, use_htb = True)
        for c in irange(1, linkopts1):
            switch1 = self.addSwitch('s%s' % c)
            for a in irange(1, linkopts2):
                switch2 = self.addSwitch('s%s' % (pow(4, a-1) + 1))
                self.addLink(switch1, switch2, **linkopts)
                for e in irange(1, linkopts3):
                     switch3 = self.addSwitch('s%s' % (pow(4, a-1) + e + 1))
                     self.addLnk(switch2, switch3, **linkopts)
                     for h in irange(1, fanout):
                        host = self.addHost('h%s' % (4*(a-1) + 2*(e-1) + h))
                        self.addLink(host, switch3, **linkopts)

def prog_assig_2():
    topo = CustomTopo(linkopts1=1, linkopts2=2, linkopts3=2, fanout=2)
    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    net.stop()

if __name__ == '_main__':
    setLogLevel('info')
    prog_assig_2()

#topos = { 'custom': ( lambda: CustomTopo() ) }


#!/usr/bin/python                                                                            
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
import time

# this is not working yet as it does not get output

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

def simpleTest(net):
    "Create and test a simple network"
    h1 = net.get('h1')
    h2 = net.get('h2')
    h1_address = h1.IP()
    result = h1.cmd('nc -l -p 3333 >outfile 2>&1 &')
    print(result)
    result = h2.cmd('cat infile | nc {h1_address} 3333 &'.format(h1_address = h1_address))
    print(result)

topos = { 'simpletopo': SingleSwitchTopo }
tests = { 'simpletest': simpleTest }

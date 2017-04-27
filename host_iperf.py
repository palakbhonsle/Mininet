from mininet.net import Mininet
from mininet.topo import Topo
from mininet.link import TCLink
from threading import Thread
from mininet.log import setLogLevel
from mininet.node import OVSController
from time import sleep
import time
import thread
class MyTopo(Topo):
	def __init__(self):
        	Topo.__init__(self)
        	leftHost1=self.addHost('h1',ip='10.0.0.1',mac='00:00:00:00ff:01')
        	leftHost2=self.addHost('h2',ip='10.0.0.2',mac='00:00:00:00ff:02')
        	rightHost1=self.addHost('h3',ip='10.0.0.3',mac='00:00:00:00ff:03')
        	rightHost2=self.addHost('h4',ip='10.0.0.4',mac='00:00:00:00ff:04')
        	leftSwitch=self.addSwitch('s1')
        	rightSwitch=self.addSwitch('s2')
		linkopts = dict(cls=TCLink)#create a dictionary to call class TCLink
        	self.addLink(leftHost1,leftSwitch,bw=10,delay='2ms',**linkopts)#call TCLink (**linkopts)
        	self.addLink(leftHost2,leftSwitch,bw=20,delay='10ms',**linkopts)
        	self.addLink(leftSwitch,rightSwitch,bw=20,delay='2ms',loss=10,**linkopts)
        	self.addLink(rightHost1,rightSwitch,bw=10,delay='2ms',**linkopts)
        	self.addLink(rightHost2,rightSwitch,bw=20,delay='10ms',**linkopts)
def iperftest():
	topo = MyTopo()
	net = Mininet(topo=topo, controller=OVSController,link=TCLink)
	net.start()#start the network
#to run command in hosts
	h1 = net.get('h1')
	h2 = net.get('h2')
	h3 = net.get('h3')
	h4 = net.get('h4')
	def function_1():
		print h3.cmd('iperf -s -i 0.5 &')#give iperf commands in host h3
		print h1.cmd('iperf -c 10.0.0.3 -t 20 -i 0.5')#generate a flow from 0 sec to 20 sec and bandwidth measured every 5 second
	def function_2():
		sleep(10)#suspends execution for 10 seconds
		print h4.cmd('iperf -s -i 0.5 &')#give iperf commands in host h4
		print h2.cmd('iperf -c 10.0.0.4 -t 20 -i 0.5')#generate a flow from 10 sec to 30 sec and bandwidth measured every 5 second
#create new t1,t2 threads
	t1 = Thread(target = function_1, args=())
	t2 = Thread(target = function_2, args=())
#start thread t1 and t2
	t1.start()
	t2.start()
#wait for t1,t2 thread to terminate
	t1.join()
	t2.join()
	net.stop()#to stop network
if __name__ == '__main__':
    setLogLevel('info')
    iperftest()


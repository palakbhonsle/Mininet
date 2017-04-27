from mininet.topo import Topo 
from mininet.net import Mininet
from mininet.link import TCLink
   
class MyTopo( Topo ):
	def __init__( self ):
		Topo.__init__( self )
		
		leftHost1 = self.addHost( 'H1', ip='10.0.0.1',mac='00:00:00:00:ff:01')
		leftHost2 = self.addHost( 'H2', ip='10.0.0.2',mac='00:00:00:00:ff:02' ) 
		rightHost1 = self.addHost( 'H3', ip='10.0.0.3',mac='00:00:00:00:ff:03')
		rightHost2 = self.addHost( 'H4', ip='10.0.0.4',mac='00:00:00:00:ff:04' )
		leftSwitch = self.addSwitch( 's1' )
		rightSwitch = self.addSwitch( 's2' )
		  

		linkopts = dict(cls=TCLink) #creating a dictionary to call class TCLink
		self.addLink( leftHost1, leftSwitch, bw=10, delay='2ms', **linkopts )#calling dictionary **linkopts 
		self.addLink( leftHost2, leftSwitch, bw=20, delay='10ms', **linkopts) 
		self.addLink( leftSwitch, rightSwitch, bw=20, delay='2ms', loss=10, **linkopts)  
		self.addLink( rightSwitch, rightHost1, bw=10, delay='2ms', **linkopts)
		self.addLink( rightSwitch, rightHost2, bw=20, delay='10ms', **linkopts )  


   
topos = { 'mytopo': ( lambda: MyTopo() ) } 

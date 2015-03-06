from mininet.topo import Topo

class MyTopo( Topo ):
    "2 switch 2 host custom topology"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's1' )
        rightSwitch = self.addSwitch( 's2' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( rightHost, rightSwitch )
        self.addLink( leftSwitch, rightSwitch )

topos = { 'mytopo': ( lambda: MyTopo() ) }

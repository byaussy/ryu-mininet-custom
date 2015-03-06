# ryu-mininet-custom
An example environment using the RYU controller, and a python script to create a custom topology consisting of 2 OVS switches and 2 hosts (one per switch)

Environment setup:

    VirtualBox
    SDN Hub Tutorial VM from http://sdnhub.org/tutorials/sdn-tutorial-vm/
    
Launch the tutorial host in VirtualBox.

Run the following commands from a terminal window:

    $ sudo mn --custom ~/ryu-mininet-custom/topo_1sw-2host.py -topo mytopo --mac --controller remote --switch ovs

Open a second terminal window and run the following commands:

    $ sudo ovs-vsctl set bridge s1 protocols=OpenFlow13
    $ /home/ubuntu/ryu/bin/ruy-manager --verbose /home/ubuntu/ryu/ryu/app/simple_switch_13.py

Switch back to the first terminal window and verify connectivity:

    mininet> h1 ping h2

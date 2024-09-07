Question1 : Define Network?
Answer : A network is a set of devices that are connected with a physical media link. In a network, two or more nodes are connected by a physical
        link  or two or more networks are connected by one or more nodes. A Network is a collection of devices connected to each other to allow 
        the sharing of data. 

Types of Networks : A computer network can transmit data by two methods- 
1) Point-to-Point: A dedicated communication channel or link connects 2 devices. The two connected devices use the full capacity of the channel as no other devices are connected. 
        ------------------            Link                -----------------
        |  WorkStation1  |  ----------------------------- | WorkStation2  |
        ------------------                                -----------------
2)Multipoint (Broadcast): More than two devices share a single link. Channel capacity is shared between connected devices. 

                    -----------------                ------------------           
                    | WorkStation1  |                |  WorkStation2  |
                    -------|----------                ---------|--------
                           |                                   |
                           |                                   |
---------------            |           link                    |
| Main Frame  |------------|--------------|--------------------|------------------
---------------                           |
                                          |
                                  --------|------------
                                  |    WorkStation3   |
                                  ---------------------
                                  
Question2 : What do you mean by network topology and explain types of them.
Answer : Network topology is the arrangement of nodes and links of a network.
1.Topologies are categorized as either physical network topology or logical network topology.
2.The topology of a network is key to determining its performance.
3.Network topology can be categorized into - Bus Topology, Ring Topology, Star Topology, Mesh Topology, Tree Topology.

Categories of network topology: 

1.Physical Topology: Describes the placement of various nodes in a computer network. In other words, it shows how network devices are physically connected. 
2.Logical Topology: Describes the idea of in what way different nodes are connected and how the data is transmitted through the network. So logical topology deals with the data flow in the network. 

1.Bus Topology
It is a multipoint connection in which every node/device is connected to a single cable (Backbone cable) via drop lines. 
Bus topology consists of two ends and data is transmitted from one end to another in a single direction i.e., bus topology is unidirectional.  
Terminators are used at the end of the cable so that the electrical signal does not bounce back. 
If the bus topology contains N nodes, then the number of cables required to connect them will be equal to N+1 where N is the number of drop lines and 1 for the backbone cable. 

                    --------------                       ------------          
                    | Nodes1     |                       |   Node 2 |
                    -------|------                       ------|-----
                           |                                   |
                           | Drop lines                        |
---------------            |           link                    |   Backbone Cable
| Terminators  |-----------|--------------|--------------------|------------------||
---------------                           |
                                          |
                                  --------|------------
                                  |    Node3          |
                                  ---------------------

Advantages: 
1.Requires a lesser number of cables. 
2.Easy to install and extend. 
3.Suitable for temporary and small networks. 

Disadvantages: 
1.Fault detection is difficult. 
2.The entire network shuts down if the main cable breaks. 
3.Limited cable length. 
4.Transmission speed decreases when more devices are added to the network. 
5.Low security. 


2. Ring Topology
In a ring topology, all the nodes are connected to form a ring such that every node will have exactly two neighbors. 
The signal is passed in one direction from one device to another device until it reaches its destination. For the signal to reach from one point to another it must travel through all the intermediate nodes. 
If the ring topology contains N nodes, then the number of cables required to connect them will be equal to N. 

Advantages:
1.Point-to-point connectivity of the nodes makes it easy to detect and identify faults.
2.Easy to install.
3.Cost-effective and inexpensive to install.
4.Extending or reducing a node from topology is easy as only two links are required to be changed.
5.The risk of collision is less as only one node is allowed to send data at a time.  

Disadvantages:
1.If a single node or a transmission line fails, the entire network breaks down.
2.Communication delay increases as the number of nodes increases.
3.Less secure.

3.Star Topology
In star topology, every device in the network is connected to a central device called hub.
All communications are done through the hub i.e. if one device wants to send data to another device, it first has to send data to the hub, and then the hub sends the data to the designated target.
If the star topology contains N nodes, then the number of cables required to connect them will be equal to N. 

Advantages:
1.Easy to install and modify.
2.Failure of one node will not affect the entire network.
3.Easy to detect the failure.
4.Less cabling is needed.

Disadvantages:
1.If the central hub breaks down, the whole network collapses.
2.Too much dependency on the central device.

4.Mesh Topology
In mesh topology, each device is connected to every other device on the network through a dedicated point-to-point link.
So, if there are N nodes in the network then every single node is connected to N-1 number of nodes. 
If the mesh topology contains N nodes, then the number of cables required to connect them will be equal to N*(N-1)/2. 

Advantages:
1.No data traffic issues because of the dedicated link between two devices.
3.Failure of a link or a device doesn’t affect the entire network.
4.Because of the dedicated point-to-point link, this topology provides high security and privacy.
5.Easy to identify the fault.

Disadvantages:
1.The amount of cables required is high.
2.The cost of implementation and maintenance is high.
3.Difficult and complicated to install and maintain.


5.Tree Topology
Tree topology is a combination of star and bus topology. In tree topology, multiple star networks are interconnected with one another using a bus network. This topology consists of a parent-child hierarchy.

Advantages:
1.Tree topology allows for the easy addition of nodes and network expansion.
2.If one segment of the network is down it doesn’t affect the other segments of the network.
3.Fault detection and correction is easy.
4.The whole network is divided into segments which makes it easy to manage and maintain.

Disadvantages:
1.The entire system is dependent on the central hub, if the central hub fails then the entire network fails.
2.Complex to design and maintain.
3.Tree topologies are expensive because of cabling.


Question3 : Define bandwidth, node and line?
Answer : Bandwidth: It is the data transfer capacity of a computer network in bits per second (Bps). 
        The term may also be used colloquially to indicate a person's capacity for tasks or deep thoughts at a point in time.
        Links and Node : A network is a connection setup of two or more computers directly connected by some physical mediums like optical fibre or coaxial cable. This physical medium of connection is known as a link, 
                        and the computers that it is connected to are known as nodes

Question4 : Explain TCP model.
Answer : It is a compressed version of the OSI model with only 4 layers. It was developed by the US Department of Defence (DoD) in the 1860s. The name of this model is based on 2 standard protocols used i.e. TCP (Transmission Control Protocol) and IP (Internet Protocol).

1. Network Access/Link layer : Decides which links such as serial lines or classic Ethernet must be used
to meet the needs of the connectionless internet layer. Ex - Sonet, Ethernet
2. Internet : The internet layer is the most important layer which holds the whole
architecture together. It delivers the IP packets where they are supposed to be delivered. Ex - IP, ICMP.
3. Transport : Its functionality is almost the same as the OSI transport layer. It
enables peer entities on the network to carry on a conversation. Ex - TCP, UDP(User Datagram Protocol)
4. Application : It contains all the higher-level protocols. Ex - HTTP, SMTP, RTP,DNS

Question5 : Layers of OSI model. 
Answer : APSTNDP

Data flows through the OSI model in a step-by-step process:
1.Application Layer: Applications create the data.
2.Presentation Layer: Data is formatted and encrypted.
3.Session Layer: Connections are established and managed.
4.Transport Layer: Data is broken into segments for reliable delivery.
5.Network Layer : Segments are packaged into packets and routed.
6.Data Link Layer: Packets are framed and sent to the next device.
7.Physical Layer: Frames are converted into bits and transmitted physically.

Question6 : Significance of Data Link Layer?
Answer : It is used for transferring the data from one node to another node.
It receives the data from the network layer and converts the data into data frames and then attaches the physical address to these frames which are sent to the physical layer.
It enables the error-free transfer of data from one node to another node.
-Functions of Data-link layer:
1.Frame synchronisation: Data-link layer converts the data into frames, and it ensures that the destination must recognize the starting and ending of each frame.
2.Flow control: Data-link layer controls the data flow within the network.
3.Error control: It detects and corrects the error occurred during the transmission from source to destination.
4.Addressing: Data-link layers attach the physical address with the data frames so that the individual machines can be easily identified.
5.Link management: Data-link layer manages the initiation, maintenance and termination of the link between the source and destination for the effective exchange of data.

Question7 : Difference between gateway and router?
Answer : A node that is connected to two or more networks is commonly known as a gateway. It is also known as a router. It is used to forward messages from one network to another. Both the gateway and router regulate the traffic in the network. Differences between gateway and router: A router sends the data between two similar networks while gateway sends the data between two dissimilar networks.

Question8 : Whar does ping comand do?
Answer : The "ping" is a utility program that allows you to check the connectivity between the network devices. You can ping devices using its IP address or name.


Question10 : what is DNS, DNS forwarder, NIC?
Answer : 
DNS:
1. DNS is an acronym that stands for Domain Name System.DNS was introduced by Paul Mockapetris and Jon Postel in 1983.
2. It is a naming system for all the resources over the internet which includes physical nodes and applications. It is used to locate resources easily over a network.
3. DNS is an internet which maps the domain names to their associated IP addresses.
4. Without DNS, users must know the IP address of the web page that you wanted to access.

DNS Forwarder : A forwarder is used with a DNS server when it receives DNS queries that cannot be resolved quickly. So it forwards those requests to external DNS 
servers for resolution. A DNS server which is configured as a forwarder will behave differently than the DNS server which is not configured as a forwarder. 

NIC : NIC stands for Network Interface Card. It is a peripheral card attached to the PC to connect to a network. Every NIC has its own MAC address that identifies 
the PC on the network. It provides a wireless connection to a local area network. NICs were mainly used in desktop computers.

Question11 : What is MAC address ?
Answer : A media access control address (MAC address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment.

Question12 : What is IP Address, private IP address, public IP address, APIPA?
Answer : 
An IP address is a unique address that identifies a device on the internet or a local network. IP stands for "Internet Protocol," which is the set of rules governing the format of data sent via the internet or local network.

Private IP Address - There are three ranges of IP addresses that have been reserved
for IP addresses. They are not valid for use on the internet. If you want to access the
internet on these private IPs, you must use a proxy server or NAT server.

Public IP Address - A public IP address is an address taken by the Internet Service
Provider which facilitates communication on the internet.

APIPA  - stands for Automatic Private IP Addressing (APIPA). It is a feature or characteristic in operating systems (eg. Windows) which enables computers to 
self-configure an IP address and subnet mask automatically when their DHCP(Dynamic Host Configuration Protocol:A DHCP Server is a network server that automatically 
provides and assigns IP addresses, default gateways and other network parameters to client devices. It relies on the standard protocol known as Dynamic Host 
Configuration Protocol) server isn't reachable.

Question13 : Difference between IPV4 and IPV6?
Answer : Difference Between IPv4 and IPv6
-IPv4:	IPv6
1.IPv4 has a 32-bit address length	IPv6 has a 128-bit address length
2.It Supports Manual and DHCP address configuration	It supports Auto and renumbering address configuration
3.In IPv4 end to end, connection integrity is Unachievable	In IPv6 end-to-end, connection integrity is Achievable
4.It can generate 4.29×10 9 address space	The address space of IPv6 is quite large it can produce 3.4×10 38 address space
5.The Security feature is dependent on the application	IPSEC is an inbuilt security feature in the IPv6 protocol
6.Address representation of IPv4 is in decimal	Address representation of IPv6 is in hexadecimal
7.Fragmentation performed by Sender and forwarding routers	In IPv6 fragmentation is performed only by the sender
8.In IPv4 Packet flow identification is not available	In IPv6 packet flow identification are Available and uses the flow label field in the header
9.In IPv4 checksum field is available	In IPv6 checksum field is not available
10.It has a broadcast Message Transmission Scheme	In IPv6 multicast and anycast message transmission scheme is available
11.In IPv4 Encryption and Authentication facility not provided	In IPv6 Encryption and Authentication are provided
12.IPv4 has a header of 20-60 bytes.	IPv6 has a header of 40 bytes fixed
13.IPv4 can be converted to IPv6	Not all IPv6 can be converted to IPv4
14.IPv4 consists of 4 fields which are separated by addresses dot (.)	IPv6 consists of 8 fields, which are separated by a colon (:)
15.IPv4’s  IP addresses are divided into five different classes. Class A , Class B, Class C, Class D , Class E.	IPv6 does not have any classes of the IP address.
16.IPv4 supports VLSM( Variable Length subnet mask ).	IPv6 does not support VLSM.
17.Example of IPv4:  66.94.29.13	Example of IPv6: 2001:0000:3238:DFE1:0063:0000:0000:FEFB

-IPv6
1.IPv6 has a 128-bit address length
2.It supports Auto and renumbering address configuration
3.In IPv6 end-to-end, connection integrity is Achievable
4.The address space of IPv6 is quite large it can produce 3.4×10 38 address space
5.IPSEC is an inbuilt security feature in the IPv6 protocol
6.Address representation of IPv6 is in hexadecimal
7.In IPv6 fragmentation is performed only by the sender
8.In IPv6 packet flow identification are Available and uses the flow label field in the header
9.In IPv6 checksum field is not available
10.In IPv6 multicast and anycast message transmission scheme is available
11.In IPv6 Encryption and Authentication are provided
12.IPv6 has a header of 40 bytes fixed
13.Not all IPv6 can be converted to IPv4
14.IPv6 consists of 8 fields, which are separated by a colon (:)
15.IPv6 does not have any classes of the IP address.
16.IPv6 does not support VLSM.
17.Example of IPv6: 2001:0000:3238:DFE1:0063:0000:0000:FEFB


Question14 : what is subnet?
Answer : A subnet is a network inside a network achieved by the process called subnetting which helps divide a network into subnets. It is used for getting a 
higher routing efficiency and enhances the security of the network. It reduces the time to extract the host address from the routing table.


Question15 : Explain Firewalls?
Answer : The firewall is a network security system that is used to monitor the incoming and outgoing traffic and blocks the same based on the firewall security 
policies. It acts as a wall between the internet (public network) and the networking devices (a private network). It is either a hardware device, software program, 
or a combination of both. It adds a layer of security to the network.

Question16 : Different types of delays?
Answer : The delays, here, means the time for which the processing of a particular packet takes place.
We have the following types of delays in computer networks:
1.Transmission Delay
2.Propagation delay
3.Queueing delay
4.Processing delay

Question17 : 3 way handshaking?
Answer : Three-Way HandShake or a TCP 3-way handshake is a process which is used in a TCP/IP network to make a connection between the server and client. 
It is a three-step process that requires both the client and server to exchange synchronisation and acknowledgment packets before the real data communication 
process starts.
Three-way handshake process is designed in such a way that both ends help you to initiate, negotiate, and separate TCP socket connections at the same time. 
It allows you to transfer multiple TCP socket connections in both directions at the same time.

Question18 : Server-side load balancer?
Answer : All backend server instances are registered with a central load balancer. A client requests this load balancer which then routes the request to one of 
the server instances using various algorithms like round-robin. AWS ELB(Elastic Load Balancing) is a prime example of server-side load-balancing that registers 
multiple EC2 instances launched in its auto-scaling group and then routes the client requests to one of the EC2 instances.

-Advantages of server-side load balancing:
1.Simple client configuration: only need to know the load-balancer address.
2.Clients can be untrusted: all traffic goes through the load-balancer where it can be looked at. Clients are not aware of the backend servers.

Question19 : RSA Algorithum?
Answer : RSA algorithm is an asymmetric cryptography algorithm. Asymmetric actually means that it works on two different keys i.e. Public Key and Private Key. 
        As the name describes, the Public Key is given to everyone and the Private key is kept private.
An example of asymmetric cryptography : A client (for example browser) sends its public key to the server and requests for some data. The server encrypts the data
using the clients public key and sends the encrypted data. Client receives this data and decrypts it. Since this is asymmetric, nobody else except the browser can decrypt the data even if a third party has the public key of the browser.

Question20 : What is HTTP and HTTPs protocols?
Answer : HTTP - HTTP is the HyperText Transfer Protocol which defines the set of rules and standards on how the information can be transmitted on the World Wide 
                Web (WWW).It helps the web browsers and web servers for communication. It is a ‘stateless protocol’ where each command is independent with respect 
                to the previous command. HTTP is an application layer protocol built upon the TCP. It uses port 80 by default. 
    HTTPS - HTTPS is the HyperText Transfer Protocol Secure or Secure HTTP. It is an advanced and a secured version of HTTP. On top of HTTP, SSL/TLS protocol is 
    used to provide security. It enables secure transactions by encrypting the communication and also helps identify network servers securely. It uses port 443 by default.

Question21 : What is SMTP protocol ?
Answer : SMTP is the Simple Mail Transfer Protocol. SMTP sets the rule for communication between servers. This set of rules helps the software to transmit emails 
        over the internet. It supports both End-to-End and Store-and-Forward methods. It is in always-listening mode on port 25.

Question22 : TCP and UDP protocol, prepare differences.
Answer : 1.TCP is a connection-oriented protocol, whereas UDP is a connectionless protocol. 
        2.A key difference between TCP and UDP is speed, as TCP is comparatively slower than UDP. Overall, UDP is a much faster, simpler, and efficient protocol, however, retransmission of lost data packets is only possible with TCP.
        3.TCP provides extensive error checking mechanisms. It is because it provides flow control and acknowledgment of data. UDP has only the basic error checking mechanism using checksums.

Question23 : What heppens whe you enter "goggle.com"(very famous question).
Answer : 
1.Check the browser cache first if the content is fresh and present in the cache display the same.
2.If not, the browser checks if the IP of the URL is present in the cache (browser and OS) if not then requests the OS to do a DNS lookup using UDP to get the corresponding IP address of the URL from the DNS server to establish a new TCP connection.
3.A new TCP connection is set between the browser and the server using three-way handshaking.
4.An HTTP request is sent to the server using the TCP connection.
5.The web servers running on the Servers handle the incoming HTTP request and send the HTTP response.
6.The browser processes the HTTP response sent by the server and may close the TCP connection or reuse the same for future requests.
7.If the response data is cacheable then browsers cache the same.
8.Browser decodes the response and renders the content.

Question24 : Hub and Switch ?
Answer : 
1.Hub:- Hub is a networking device which is used to transmit the signal to each port
    (except one port) to respond from which the signal was received. Hub is operated on a Physical layer. In this packet filtering is not available.
    It is of two types: Active Hub, Passive Hub.
2.Switch:- Switch is a network device which is used to enable the connection establishment and connection termination on the basis of need. Switch is operated on 
the Data link layer. In this packet filtering is available. It is a type of full duplex transmission mode and it is also called an efficient bridge

Question25 : VPN, advantages and disadvantages of it. 
Answer : VPN (Virtual Private Network) : VPN or the Virtual Private Network is a private WAN
(Wide Area Network) built on the internet. It allows the creation of a secured tunnel
(protected network) between different networks using the internet (public network). By using the VPN, a client can connect to the organisation’s network remotely.

Advantages of VPN :
1. VPN is used to connect offices in different geographical locations remotely and is
cheaper when compared to WAN connections.
2. VPN is used for secure transactions and confidential data transfer between
multiple offices located in different geographical locations.
3. VPN keeps an organisation’s information secured against any potential threats or
intrusions by using virtualization.
4. VPN encrypts the internet traffic and disguises the online identity

Disadvantages of VPN :
1. Not designed for continuous use
2. Complexity prevents scalability
3. Lack of granular security
4. Unpredictable performance
5. Unreliable availability


Question26 : Explain LAN?
Answer : A local area network (LAN) is a collection of devices connected together in one physical location, such as a building, office, or home. A LAN can be small
 or large, ranging from a home network with one user to an enterprise network with thousands of users and devices in an office or school.

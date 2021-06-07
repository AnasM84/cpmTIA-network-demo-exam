from datetime import datetime
import sys
print("""
                         _____ _____  ___                _                      _                _                                                 
                        |_   _|_   _|/ _ \              | |                    | |     _        | |                                                
  ___ ___  _ __ ___  _ __ | |   | | / /_\ \   _ __   ___| |___      _____  _ __| | ___| |_    __| | ___ _ __ ___   ___     _____  ____ _ _ __ ___  
 / __/ _ \| '_ ` _ \| '_ \| |   | | |  _  |  | '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ /_   _|  / _` |/ _ \ '_ ` _ \ / _ \   / _ \ \/ / _` | '_ ` _ \ 
| (_| (_) | | | | | | |_) | |  _| |_| | | |  | | | |  __/ |_ \ V  V / (_) | |  |   <  |_|   | (_| |  __/ | | | | | (_) | |  __/>  < (_| | | | | | |
 \___\___/|_| |_| |_| .__/\_/  \___/\_| |_/  |_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_\        \__,_|\___|_| |_| |_|\___/   \___/_/\_\__,_|_| |_| |_|
                    | |                                                                                                                            
                    |_|                                                                                                                            


""")
print("""by s_.y._s
1= A
2 = B
3- C
4- D
if you see (Choose all that apply) enter the number like this = if 2 number = 12 <-- exp
""")



print("                                           exam start at  "+str(datetime.now()))


point = 0
q1 = input("""
1.What is the basic purpose of a local area network (LAN)?

A.    To interconnect networks in several different buildings
B.    To connect one or more computers together so they can share resources
C.    To interconnect 2 to 10 routers
D.    To make routers unnecessary

An : """) 
if q1 == '2':
	print("\nnice [!]")
	point += 1
elif q1 == 1 or 3 or 4 :
	print("wrong [-] info : LANs generally have a geographic scope of a single building or smaller. They can be simple (two hosts) to complex (with thousands of hosts) ")
q2 = input("""
2.Which of the following describes a VLAN?

A.    It is a device that provides IP addresses to hosts.
B.    It uses firewalls.
C.    It virtually separates subnets using switches.
D.    It virtually separates subnets using routers

An : """)
if q2 == '3':
	print("\nnice [!]")
	point += 1
elif q2 == 2 or 1 or 4  :
	print("wrong [-] info :Virtual LANs (VLANs) separate subnets (Layer 3 networks) using switches instead of routers.")
else:
	print("error wrong output [!] -> exit....")
	sys.exit()	
q3 =input("""
3.IP resides at which layer of the OSI model?

A.    Application
B.    Data Link
C.    Network
D.    Physical

An : """)
if q3 == '3':
	print("\nnice [!]")
	point += 1
elif q3 == 1 or 2 or 4  :
	print("wrong [-] info :IP is a Network-layer protocol. Internet Explorer is an example of an Application layer protocol; Ethernet is an example of a Data Link–layer protocol; and T1 can be considered a Physical-layer protocol")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q4 = input("""
4.Layer 2 of the OSI model is named ___________________.

A.    Application layer
B.    Network layer
C.    Transport layer
D.    Data Link layer

An : """) 
if q4 == '4':
	print("\nnice [!]")
	point += 1
elif q4 == 1 or 2 or 3   :
	print("wrong [-] info :Layer 2 of the OSI model is the Data Link layer, which provides the physical transmis-sion of the data and handles error notification, network topology, and flow control.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q5 =input("""
5.Which RG rating of coax is used for cable modems?

A.    RG -59
B.    RG -58
C.    RG -6
D.    RG -8

An : """)
if q5 == '4':
	print("\nnice [!]")
	point += 1
elif q5 == 1 or 2  or 3   :
	print("wrong [-] info :Cable modems use RG-6 coax cables")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q6 =input("""
6.Which UTP wiring uses four twisted wire pairs (eight wires) and is rated for 250MHz?

A.    Category 3 UTP
B.    Category 5 STP
C.    Category 5 UTP
D.    Category 6 UTP

An : """) 
if q6 == '4':
	print("\nnice [!]")
	point += 1
elif q6 == 1 or 2 or 3   :
	print("wrong [-] info :To get the high data-transfer speed, like 1Gbps, you need to use a wire standard that is highly rated, such as Category 5e or Category 6")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q7 =input("""
7.If you are running half-duplex Internet, which of the following is true. (Choose all that apply)? 

A.    Your digital signal cannot transmit and receive data at the same time.
B.    Hosts use the CSMA/CD protocol to prevent collisions.
C.    The physical connection consists of one wire pair.
D.    All of the above

An : """) 
if q7 == '4':
	print("\nnice [!]")
	point += 1
elif q7 == 1 or 2 or 3   :
	print("wrong [-] info :A, B, and C are true. With half-duplex, you are using one wire pair with a digital signal either transmitting or receiving (but not both at once). Carrier Sense Multiple Access with Collision Detection (CSMA/CD) helps packets that are transmitted simultaneously from different hosts share bandwidth evenly.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q8 =input("""
8.You need to connect a hub to a switch. You don’t like this idea because you know that it will create congestion. What type of cable do you need to use to connect the hub to the switch?

A.    EtherIP
B.    Crossover
C.    Straight-through
D.    Cable Sense, Multiple Access

An : """) 
if q8 == '2':
	print("\nnice [!]")
	point += 1
elif q8 == 1 or 3 or 4   :
	print("wrong [-] info :To connect two switches together or a hub to a switch, you need a crossover cable")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q9 =input("""
9.Your boss asks you why you just put in a requisition to buy a bunch of switches. He said he just bought you a bunch of hubs five years ago! Why did you buy the switches? 

A.    Because each switch port is its own collision domain.
B.    The cable connecting devices to the hub wore out, and switches were cheaper than new cable.
C.    There were too many broadcast domains, and a switch breaks up broadcast domains by default.
D.    The hubs kept repeating signals but quit recognizing frames and data structures.

An : """) 
if q9 == '1':
	print("\nnice [!]")
	point += 1
elif q9 == 2 or 3 or 4   :
	print("wrong [-] info :For the most part, switches are not cheap; however, one of the biggest benefits of using switches instead of hubs in your internetwork is that each switch port is actually its own collision domain. A hub creates one large collision domain. Switches still can’t break up broadcast domains (do you remember which devices do?). Hubs do not recognize frames and data structures but switches do")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q10 =input("""
10.  Which device would connect network segments together, creating separate collision domains for each segment but only a single broadcast domain?
A.    Hub
B.    Router
C.    Switch
D.    Modem

An : """) 
if q10 == '3':
	print("\nnice [!]")
	point += 1
elif q10 == 1 or 2 or 4   :
	print("wrong [-] info : A switch creates separate collision domains for each port but does not break up broad-cast domains by default")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q11 =input("""
11.   Most Application-layer protocols only use UDP or TCP at the Transport layer. Which of the following could use both? 
A.    TCP
B.    Microsoft Word
C.    Tel net
D.    DNS

An : """) 
if q11 == '4':
	print("\nnice [!]")
	point += 1
elif q11 == 1 or 2 or 3   :
	print("wrong [-] info :DNS uses TCP for zone exchanges between servers and UDP when a client is trying to resolve a hostname to an IP address")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q12 =input("""
12.  HTTP, FTP, and Telnet work at which layer of the OSI model?

A.    Application
B.    Presentation
C.    Session
D.    Transport

An : """) 
if q12 == '1':
	print("\nnice [!]")
	point += 1
elif q12 == 2 or 3 or 4   :
	print("wrong [-] info :   HTTP, FTP and Telnet use TCP at the Transport layer; however, they are all Application-layer protocols, so the Application layer is the best answer for this question")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q13 =input("""
13.  IPv6 uses multiple types of addresses. Which of the following would describe an anycast address used by an IPv6 host?

A.    Communications are routed to the most distant host that shares the same address.

B.    Packets are delivered to all interfaces identified by the address. This is also called one-to-many addressing.

C.    This address identifies multiple interfaces, and the anycast packet is only delivered to one address. This address can also be called one-to-one-of-many. 

D.    Anycast is a type of broadcast.

An : """) 
if q13 == '1':
	print("\nnice [!]")
	point += 1
elif q13 == 2 or 3 or 4  :
	print("wrong [-] info :   HTTP, FTP and Telnet use TCP at the Transport layer; however, they are all Application-layer protocols, so the Application layer is the best answer for this question")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q14 =input("""
14.  Which of the following IP addresses are not allowed on the Internet? (Choose all that apply.)[2 number]

A.    11.255.255.1
B.    10.1.1.1
C.    172 .33. 255.0
D.    192.l68.0.1

An : """) 
if q14 == '24':
	print("\nnice [!]")
	point += 1
elif q14 == 12 or 23 or 34 or 13 or 14 or 23  :
	print("wrong [-] info :The addresses in the range 10.0.0.0 through 10.255.255.255, and 172.16.0.0 through 172.31.255.255, as well as 192.168.0.0 through 192.168.255.255 are all considered private, based on RFC 1918. Use of these addresses on the Internet is prohibited so that they can be used simultaneously in different administrative domains without concern for conflict.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q15 =input("""
15.  What is the subnetwork address for a host with the IP address 200.10.5.168/28?

A.    200.10.5.156
B.    200.10.5.132
C.    200.10.5.160
D.    200.10.5.0
E.    200.10.5.255

An : """) 
if q15 == '3':
	print("\nnice [!]")
	point += 1
elif q15 == 1 or 2 or 4 or 5 :
	print("wrong [-] info :This is a pretty simple question. A /28 is 255.255.255.240, which means that our block size is 16 in the fourth octet. 0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, and so on. The host is in the 1604 subnet")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q16 =input("""
16.  If you wanted to verify the local IP stack on your computer, what would you do? 

A.    ping 127.0.0.0
B.    ping 127.0.0.1
C.     telnet 1.0.0.127
D.    ping 127.0.0.255
E.    telnet 255.255.255.255

An : """) 
if q16 == '2':
	print("\nnice [!]")
	point += 1
elif q16 == 1 or 3 or 4 or 5 :
	print("wrong [-] info :To test the local stack on your host, ping the loopback interface of 127.0.0.1. ")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q17 =input("""
17.   The OSI model uses an encapsulation method to describe the data as it is encapsulated at each layer of the OSI. What is the encapsulation named at the Data Link layer?  

A.    Bits
B.    Packets
C.    Frames
D.    Data
E.    Segments

An : """) 
if q17 == '3':
	print("\nnice [!]")
	point += 1
elif q17 == 1 or 2 or 4 or 5 :
	print("wrong [-] info :PThe Data Link layer is responsible for encapsulating IP packets into frames and for providing logical network addresses")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q18 =input("""
18.  Where does a Data Link layer frame have to carry a Network layer packet if the packet is destined for a remote network? 

A.    Router
B.    Physical medium
C.    Switch
D.    Another host

An : """) 
if q18 == '1':
	print("\nnice [!]")
	point += 1
elif q18 == 2 or 3 or 4   :
	print("wrong [-] info :Packets specifically have to be carried to a router in order to be routed through a network")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q19 =input("""
19.  Which of the following are not Distance Vector routing protocols? (Choose all that apply.)[2 number]

A.   OSPF
B.    RIP
C.    RIPv2
D.    IS-IS

An : """) 
if q19 == '14':
	print("\nnice [!]")
	point += 1
elif q19 == 12 or 23 or 13 or 24 or 34 :
	print("wrong [-] info :RIP and RIPv2 are Distance Vector routing protocols. OSPF and IS-IS are Link State.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q20 =input("""
20.  Which of the following uses both Distance Vector and Link State properties?

A.   IGRP
B.    OSPF
C.    R IPv1
D.    EIGRP
E.    IS-IS

An : """) 
if q20 == '4':
	print("\nnice [!]")
	point += 1
elif q20 == 1 or 2 or 3 or 5 :
	print("wrong [-] info :EIGRP is called a hybrid routing protocol because it uses the characteristics of both Distance Vector and Link State routing protocols. However, EIGRP can only be run on Cisco routers and is not vendor-neutral.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q21 =input("""
21.  You need to break up broadcast domains in a Layer 2 switched network. What strategy will you use? 

A.    Implement a loop-avoidance scheme
B.    Create a flatter network structure using switches
C.    Create a VLAN
D.    Disable spanning tree on individual ports

An : """) 
if q21 == '3':
	print("\nnice [!]")
	point += 1
elif q21 == 1 or 2 or 4   :
	print("wrong [-] info :Virtual LANs break up broadcast domains in Layer 2 switched internetworks.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q22 =input("""
22.  Why do most switches run the Spanning Tree Protocol by default? 

A.    It monitors how the network is functioning.
B.    It stops data from forwarding until all devices are updated.
C.    It prevents switching loops.
D.    It manages the VLAN database

An : """) 
if q22 == '3':
	print("\nnice [!]")
	point += 1
elif q22 == 1 or 2 or 4   :
	print("wrong [-] info :The Spanning Tree Protocol (STP) was designed to stop Layer 2 loops. All enterprise model switches have STP by default.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q23 =input("""
23.  Which of the following describes MIMO correctly? 

A.    A protocol that requires acknowledgment of each and every frame

B.    A data-transmission technique in which several frames are sent by several antennae over several paths and are then recombined by another set of antennae

C.    A modulation technique that allows more than one data rate

D.    A technique that packs smaller packets into a single unit, which improves throughput

An : """) 
if q23 == '2':
	print("\nnice [!]")
	point += 1
elif q23 == 1 or 3 or 4  :
	print("wrong [-] info :Part of the 802.11n wireless standard, MIMO sends multiple frames by several antennae over several paths; they are then recombined by another set of antennae to optimize through-put and multipath resistance. This is called spatial multiplexing")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q24 =input("""
24.  Which two practices help secure your wireless access points from unauthorized access?[2 number]

A.    Assigning a private IP address to the AP
B.    Changing the default SSID value
C.    Configuring a new administrator password
D.    Changing the mixed-mode setting to single mode
E.    Configuring traffic filtering

An : """) 
if q24 == '23':
	print("\nnice [!]")
	point += 1
elif q24 == 12 or 34 or 45 :
	print("wrong [-] info :At a minimum, you need to change the default SSID value on each AP and configure new usernames and passwords on the AP.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q25 =input("""
25.  IPSec is defined at what layer of the OSI model? 

A.     Network
B.    Physical
C.    Layer 4
D.    Layer 7

An : """) 
if q25 == '1':
	print("\nnice [!]")
	point += 1
elif q25 == 2 or 3 or 4   :
	print("wrong [-] info :PSec works at the Network layer of the OSI model (Layer 3) and secures all applica-tions that operate above it (Layer 4 and above). Additionally, because it was designed by the IETF and designed to work with IPv4 and IPv6, it has broad industry support and is quickly becoming the standard for VPNs on the Internet.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q26 =input("""
26.  You want your users to log in and authenticate before they can get onto your network. Which of the following services would you use?

A.   RADIUS
B.    TACACS+
C.    Virtual Network Computing
D.    Remote desktop protocol

An : """) 
if q26 == '1':
	print("\nnice [!]")
	point += 1
elif q26 == 2 or 3 or 4   :
	print("wrong [-] info :   RADIUS combines user authentication and authorization into one profi")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q27 =input("""
27.  Someone calls you and asks for your bank-account number because the bank is having problem with your account. You give them this information and later find out that you  were scammed. What type of attack is this? 

A.   Phishing
B.    Calling-scam
C.    Analog-scam
D.    Trust-exploration attack
E.    Man-in-the-middle attack
F.Rogue access point

An : """) 
if q27 == '1':
	print("\nnice [!]")
	point += 1
elif q27 == 2 or 3 or 4 or 5 or 6 :
	print("wrong [-] info :Social engineering or phishing refers to the act of attempting to illegally obtain sensitive information by pretending to be a credible source. Phishing usually takes one of two forms: an email or a phone call.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q28 =input("""
28.  Which three of the following are types of denial of service attacks?

A.    Ping of Death
B.    Stacheldraht
C.    SYN flood
D.    Virus FloodSyn

An : """) 
if q28 == '123':
	print("\nnice [!]")
	point += 1
elif q28 == 124 or 234 or 342 or 432:
	print("wrong [-] info :A denial of service (DoS) attack prevents users from accessing the system. All of the above are all possible denial of service attacks except Virus FloodSyn")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q29 =input("""
29.  You want to stop a hacker in their tracks. Which of the following devices are proactive in providing this service? 

A.    Access control list (ACL)
B.    Content filtering
C.    Security zones
D.    Intrusion Prevention System (IPS)
E.    Network Address Translation
F.Virtual LAN’s

An : """) 
if q29 == '4':
	print("\nnice [!]")
	point += 1
elif q29 == 1 or 2 or 4 or 5 or 6 :
	print("wrong [-] info :Changing network configurations, terminating sessions, and deceiving the attacker are all actions that can be taken by an Intrusion Prevention System (IPS) device. These are all proactive approaches to security.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q30 =input("""
30.  You connected your company to the Internet, and security is a concern. What should  you install? 

A.    Higher-quality cables
B.    Firewall
C.    DNS
D.    Switches

An : """) 
if q30 == '2':
	print("\nnice [!]")
	point += 1
elif q30 == 1 or 3 or 4   :
	print("wrong [-] info :Firewalls help provide perimeter network security by allowing or denying connections and types of traffic in or out of the network. ")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q31 =input("""
31.  Which of the following are WAN protocols or technologies? (Choose all that apply.)

A.    ATM
B.    ISDN
C.    MPLS
D.    RIP

An : """) 
if q31 == '123':
	print("\nnice [!]")
	point += 1
elif q31 == 124 or 234 or 342 or 432:
	print("wrong [-] info :Routing Information Protocol (RIP) is not a WAN protocol, but a routing proto-col used in local area connections.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q32 =input("""
32.  The rate at which the frame-relay switch agrees to transfer data is referred to as ___________________. 

A.   BE
B.    FECN
C.    CIR
D.    BECN

An : """) 
if q32 == '3':
	print("\nnice [!]")
	point += 1
elif q32 == 1 or 2 or 4  :
	print("wrong [-] info :The Committed Information Rate (CIR) is the rate, in bits per second, at which the frame-relay switch agrees to transfer data")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q33 =input("""
33.  Which two arp utility switches perform the same function? [2 number]

A.–g
B.–A
C.–d
D.–a
E.  -h
F.  -b

An : """) 
if q33 == '14':
	print("\nnice [!]")
	point += 1
elif q33 == 12 or 23 or 34 or 45 :
	print("wrong [-] info :The arp utility’s –a and –g switches perform the same function. They both show the current ARP cache")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q34 =input("""
34.  You need to purge and reload the remote NetBIOS name table cache. Which nbtstat utility switch will you use? 

A.–r
B.–R
C./r
D./R
E.  -a
F.  -A

An : """) 
if q34 == '2':
	print("\nnice [!]")
	point += 1
elif q34 == 1 or 3 or 4   :
	print("wrong [-] info :To purge and reload the remote NetBIOS name cache, you must use nbtstat –R. Remember that the R must be uppercase, and it will not work correctly without the hyphen before it")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q35 =input("""
35.  Which tool is used to attach ends to network cables? 

A.    Punch-down tool
B.    Crimper
C.    VLAN tool
D.    Strippers
E.    ARP tool

An : """) 
if q35 == '2':
	print("\nnice [!]")
	point += 1
elif q35 == 1 or 3 or 4   :
	print("wrong [-] info :A wire crimper or crimper is used to attach ends onto different types of network cables.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q36 =input("""
36.  You are using a TDR. Which three of the following actions can you do with this device? [3 number]

A.    Estimate cable lengths
B.    Find splice and connector locations and their associated loss amounts
C.    Display unused services
D.    Define cable-impedance characteristics

An : """) 
if q36 == '124':
	print("\nnice [!]")
	point += 1
elif q36 == 123 or 321 or 213 :
	print("wrong [-] info :Due to sensitivity to any variation and impedance to cabling, answers A, B and D are all reasons you’d use a TDR")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q37 =input("""
37.  Which of the following are considered cabling issues? (Choose all that apply  [3 number])

A.   Crosstalk
B.    Shorts
C.    Open impedance mismatch
D.    DNS configurations

An : """) 
if q37 == 123:
	print("\nnice [!]")
	point += 1
elif q37 == 124 or 234 or 342 or 432 :
	print("wrong [-] info :Because most of today’s networks still consist of large amounts of copper cable, they can continue to suffer from the physical issues (the options are not a complete list) that have plagued all networks since the very beginning of networking.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q38 =input("""
38.  A workstation gives an error message to a user. The message states that a duplicate IP address has been detected on the network. After developing a hypothesis, what should the next step be according to the standard troubleshooting model?

A.    Test and observe an action plan.
B.    Determine if anything has changed.
C.    Implement an action plan.
D.    Document the solution and the entire process.

An : """) 
if q38 == '3':
	print("\nnice [!]")
	point += 1
elif q38 == 1 or 2 or 4  :
	print("wrong [-] info :Creating an action plan and a solution, and identifying the potential effects, would be the next step according to the standard troubleshooting model.")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q39 =input("""
39.  Which network-performance-optimization technique can delay packets that meet certain criteria to guarantee usable bandwidth for other applications? 

A.    Traffic shaping
B.    Jitter control
C.    Logical network mapping
D.    Load balancing
E.    Access lists

An : """) 
if q39 == '1':
	print("\nnice [!]")
	point += 1
elif q39 == 2 or 3 or 4  :
	print("wrong [-] info :Traffic shaping, also known as packet shaping, is another form of bandwidth optimization. ")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
q40 =input("""
40.  You need to optimize network traffic by spreading it across multiple connections. Which strategy should be used? 
A.    Load balancing
B.    Traffic shaping
C.    Add VLAN’s
D.    A 1Gbps connection
E.    Following the regulations

An : """) 
if q40 == '1':
	print("\nnice [!]")
	point += 1
elif q40 ==  2 or 3 or 4 :
	print("wrong [-] info :Load balancing refers to a technique used to spread work out to multiple computers, net-work links, or other devices. You can load-balance work on servers by clustering servers so that multiple machines all provide the same service. ")

else:
	print("error wrong output [!] -> exit....")
	sys.exit()
print("\nexam finsh at  "+str(datetime.now()))
print("\nand you got {}/40".format(point))

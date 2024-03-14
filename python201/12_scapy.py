"""
scapy - packet manipulation library
- can forge, decode, send, and capture packets at low level
- all parts of the packet you send and receive with scapy can be modified and inspect
- has its own cli

- pip install scapy

- NOTE:  Need libpcap installed!!!

NEED REVIEW THIS TOPIC WITH NETWORK PROTOCOLS...

References
----------------
https://en.wikipedia.org/wiki/Internet_protocol_suite
https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol
https://en.wikipedia.org/wiki/Address_Resolution_Protocol
https://en.wikipedia.org/wiki/Broadcasting_(networking)
https://en.wikipedia.org/wiki/Pcap
"""

from scapy.all import *

# ip_layer = IP(dst="247ctf.com")
# icmp_layer = ICMP()

# packet = ip_layer / icmp_layer

# r = send(packet)

# print(packet.show())

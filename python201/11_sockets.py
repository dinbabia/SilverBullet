"""
sockets - a bidirectional communication channel
- send data and can receive data
- can communicate within a process between process or between different systems on a network
- for this lesson, we focus on tcp.
- sockets can be also used for different protocols

References
------------------
https://en.wikipedia.org/wiki/Transmission_Control_Protocol
https://en.wikipedia.org/wiki/Network_socket
"""

import socket

ip = socket.gethostbyname('247ctf.com')
print(ip)

# AF_INET - transport mechanism , ipv4
# SOCK_STREAM - connection oriented protocol , tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('247ctf.com', 80))
# once we are connected, we can send and receive data in this socket

# Send request
s.sendall(b"HEAD / HTTP/1.1\r\nHost: 247ctf.com\r\n\r\n")
# Receive response
print(s.recv(1024).decode())

s.close()


# ----- client - server

client = False
server = False
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if server:
    s.bind(("127.0.0.1", port))
    s.listen()

    while True:
        connect, addr = s.accept()
        connect.send(b"YEYYY, made it to the socket")
        connect.close()

if client:
    s.connect(("127.0.0.1", port))
    print(s.recv(1024))
    s.close()

for p in [22, 80, 139, 443, 445, 8080]:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    # connect_ex is like connect but this method returns an error rather than raising an exception
    result = s.connect_ex(("127.0.0.1", port))
    if result == 0:
        print(f"Port {p} is open!")
    else:
        print(f"Port {p} is close!")
    s.close()

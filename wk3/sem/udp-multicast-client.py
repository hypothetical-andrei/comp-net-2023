import socket
import struct
# Set up the multicast address and port number
multicast_group = '224.0.0.1'
server_address = ((multicast_group, 5001))

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Add the socket to the multicast group
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive data in a loop
while True:
    data, address = sock.recvfrom(1024)
    print(f'Received {len(data)} bytes from {address}: {data.decode()}')

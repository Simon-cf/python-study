from socket import *


udp_socket = socket(AF_INET, SOCK_DGRAM)
local_addr = ('', 3000)
udp_socket.bind(local_addr)
udp_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, True)
udp_socket.sendto("大家好，我是崔帆".encode(), ("255.255.255.255", 9090))
udp_socket.close()
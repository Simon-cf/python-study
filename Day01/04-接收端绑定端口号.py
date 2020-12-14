from socket import *

if __name__ == '__main__':
    local_addr = ("", 3000)
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(local_addr)
    udp_socket.sendto("hahaha".encode(), ('127.0.0.1', 8080))
    data = udp_socket.recvfrom(1024)
    print("接收到来自%s的数据【%s】" % (data[1], data[0].decode(encoding='utf-8', errors='ignore')))

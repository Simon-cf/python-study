import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
udp_socket.bind(('', 3000))
udp_socket.sendto("我要好好学计算机".encode(), ('127.0.0.1', 8080))
data = udp_socket.recvfrom(1024)
print("收到了来自%s的信息【%s】" % (data[1], data[0].decode(encoding='gbk', errors='ignore')))

udp_socket.close()
"""
1.导入模块
2.创建套接字

4.发送数据
5.关闭套接字

"""

# 1.导入模块
import socket

# 2.创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 4.发送数据
message = input("请输入你想要发送的内容：")
udp_socket.sendto(message.encode('utf-8'), ('172.20.10.1', 8081))
# 5.接收数据
recv_data, ip_port = udp_socket.recvfrom(1024)
print(recv_data.decode())
# 6.关闭套接字
udp_socket.close()

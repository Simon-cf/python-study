"""
1.导入模块
2.创建套接字
3.绑定端口
4.发送数据
5.接收数据
6.关闭套接字
"""

# 1.导入模块
import socket
# 2.创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3.绑定端口
udp_socket.bind(('', 5000))
# 4.发送数据
other_addr = ('172.20.10.8', 8080)
while True:
    message = input("请输入您要发给对方的信息：")
    if not message:
        break
    udp_socket.sendto(message.encode(), other_addr)
    # 5.接收数据
    recv_data, ip_port = udp_socket.recvfrom(1024)
    print("收到来自{}的信息【{}】".format(ip_port,recv_data.decode()))
# 6.关闭套接字
udp_socket.close()
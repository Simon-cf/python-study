"""
导入模块
创建套接字
发送数据
接收数据
关闭套接字
"""

# 导入模块
import socket

# 创建套接字
# 需要指定两个参数，通信协议 ipv4 AF_INET / ipv6 AF_INET6 传输方式 SOCK_DGRAM udp(面向无连接) SOCK_STREAM tcp
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
udp_socket.bind(('', 5000))
while True:
    # 发送数据
    message = input()
    udp_socket.sendto(message.encode(), ('10.35.223.23', 6000))
    recv_data = udp_socket.recvfrom(1024)
    print("收到来自%s 的 [%s] " % (recv_data[1], recv_data[0].decode()))
    if not recv_data[0]:
        break
# 关闭套接字
udp_socket.close()
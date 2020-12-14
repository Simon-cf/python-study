"""
1.导入模块
2.创建套接字
3.发送数据
4.接收数据
5.关闭套接字


"""

# 1.导入模块
import socket

# 2.创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3.发送数据
while True:
    message = input("请输入您想要发送的内容:")
    udp_socket.sendto(message.encode(), ('172.20.10.1', 8081))
    # 4.接收数据
    recv_data, ip_port = udp_socket.recvfrom(1024)
    if not recv_data:
        break
    recv_text = recv_data.decode()
    print("收到{}发来的消息【{}】".format(ip_port, recv_text))
# 5.关闭套接字
udp_socket.close()
